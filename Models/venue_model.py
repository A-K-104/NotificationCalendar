from typing import Union
from Commons.Entities.Venue import Venue
from Commons.Utiles.db_session_wrapper import with_db_session


@with_db_session
def get_venue_by_id(session, venue_id: int) -> Union[dict, None]:
    venue = session.query(Venue).get(venue_id)
    if venue is not None:
        return venue.to_dict()
    return None


@with_db_session
def create_venue(session, **kwargs) -> dict:
    venue = Venue.create(session, **kwargs)
    return venue.to_dict()


@with_db_session
def update_venue_by_id(session, venue_id: int, **kwargs) -> Union[dict, None]:
    venue = session.query(Venue).get(venue_id)
    if venue:
        venue.update(session, **kwargs)
        return venue.to_dict()
    return None


@with_db_session
def delete_venue_by_id(session, venue_id: int) -> bool:
    venue = session.query(Venue).get(venue_id)
    if venue:
        session.delete(venue)
        session.commit()
        return True
    return False
