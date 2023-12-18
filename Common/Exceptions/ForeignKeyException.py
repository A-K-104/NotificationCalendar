class ForeignKeyException(Exception):
    message: str = "Linked object is not present in table"
    error_code: int = 415
