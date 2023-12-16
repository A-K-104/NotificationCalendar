class ContentException(Exception):
    message: str = "Invalid content type, expecting JSON"
    error_code: int = 415
