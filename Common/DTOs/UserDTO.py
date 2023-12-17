from datetime import datetime


class UserDTO:
    def __init__(self,
                 element_id: int,
                 username: str,
                 role: str,
                 created_on: datetime
                 ):
        self.element_id = element_id
        self.username = username
        self.role = role
        self.created_on = created_on

    def to_dict(self):
        return {
            "element_id": self.element_id,
            "username": self.username,
            "role": self.role,
            "created_on": self.created_on
        }
