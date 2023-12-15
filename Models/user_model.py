from typing import Union
from Commons.Entities.User import User
from Commons.Utiles.db_session_wrapper import with_db_session


@with_db_session
def get_user_by_id(session, user_id: int) -> Union[dict, None]:
    user = session.query(User).get(user_id)
    if user is not None:
        user.to_dict()
    return None


@with_db_session
def create_user(session, username: str, role: str) -> dict:
    user = User.create(session, username, role)
    return user.to_dict()


@with_db_session
def update_user_by_id(session, user_id: int, **kwargs) -> Union[dict, None]:
    user = session.query(User).get(user_id)
    if user:
        user.update(session, **kwargs)
    return user.to_dict()


@with_db_session
def delete_user_by_id(session, user_id: int) -> bool:
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
