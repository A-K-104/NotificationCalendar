class NotFoundException(Exception):
    message: str = "Not found"
    error_code: int = 404
