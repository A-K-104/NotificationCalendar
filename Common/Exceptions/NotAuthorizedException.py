class NotAuthorizedException(Exception):
    message: str = "Not authorized"
    error_code: int = 401
