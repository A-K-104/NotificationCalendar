from typing import Union
from Common.Entities.Event import Event
from Common.Utiles.db_session_wrapper import with_db_session


@with_db_session
def get_event_by_id(session, event_id: int) -> Union[dict, None]:
    event = session.query(Event).get(event_id)
    if event is not None:
        return event.to_dict()
    return None


@with_db_session
def get_all_events(session) -> Union[list, None]:
    events = session.query(Event).all()
    if events is not None:
        return [event.to_dict() for event in events]
    return None


@with_db_session
def create_event(session, user_id: int, **kwargs) -> dict:
    event = Event.create(session, user_id, **kwargs)
    return event.to_dict()


@with_db_session
def update_event_by_id(session, event_id: int, **kwargs) -> Union[dict, None]:
    event = session.query(Event).get(event_id)
    if event:
        event.update(session, **kwargs)
        return event.to_dict()
    return None


@with_db_session
def delete_event_by_id(session, event_id: int) -> bool:
    event = session.query(Event).get(event_id)
    if event:
        session.delete(event)
        session.commit()
        return True
    return False
