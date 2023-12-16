from datetime import datetime


class UserDTO:
    def __init__(self,
                 username: str,
                 role: str,
                 created_on: datetime
                 ):
        self.username = username
        self.role = role
        self.created_on = created_on

    def to_dict(self):
        return {
            "username": self.username,
            "role": self.role,
            "created_on": self.created_on
        }
