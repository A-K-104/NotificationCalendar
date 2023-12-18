class NotValidException(Exception):
    message: str = "Not Valid"
    error_code: int = 500
