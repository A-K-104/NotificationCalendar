class NotInEnumException(Exception):
    message: str = "Enum wasn't found"
    error_code: int = 400
