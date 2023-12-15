from typing import Union
from Commons.Entities.User import User
from Commons.Utiles.db_session_wrapper import with_db_session


@with_db_session
def get_user_by_id(session, user_id: int) -> Union[User, None]:
    return session.query(User).get(user_id)


@with_db_session
def create_user(session, username: str, role: str) -> User:
    user = User.create(session, username, role)
    return user


@with_db_session
def update_user_by_id(session, user_id: int, **kwargs) -> Union[User, None]:
    user = session.query(User).get(user_id)
    if user:
        user.update(session, **kwargs)
    return user


@with_db_session
def delete_user_by_id(session, user_id: int) -> None:
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
