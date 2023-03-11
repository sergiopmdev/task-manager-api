from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    """
    Exception to be thrown when trying
    to write the user to the database
    when the user already exists
    """

    pass
