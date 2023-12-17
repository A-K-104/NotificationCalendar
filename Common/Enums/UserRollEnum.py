from enum import Enum


class UserRollEnum(Enum):
    ADMIN = 1
    USER = 2

    def __eq__(self, other: str):
        return self.name == other

    def __str__(self):
        return self.name

    @classmethod
    def __contains__(cls, item):
        return any(item == member.name for member in cls)

