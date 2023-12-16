from datetime import datetime


class UserDTO:
    def __init__(self,
                 el_id: int,
                 username: str,
                 role: str,
                 created_on: datetime
                 ):
        self.el_id = el_id
        self.username = username
        self.role = role
        self.created_on = created_on

    def to_dict(self):
        return {
            "el_id": self.el_id,
            "username": self.username,
            "role": self.role,
            "created_on": self.created_on
        }
