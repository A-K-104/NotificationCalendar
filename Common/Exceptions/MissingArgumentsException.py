class MissingArgumentsException(Exception):
    message: str = "missing arguments"
    error_code: int = 400
