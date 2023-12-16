class NameAlreadyUsedException(Exception):
    message: str = "Name already exist"
    error_code: int = 400
