from typing import Dict

from models.User import User
from utils.Database import Database


class UserHandler:
    """
    Handler of the set of data and actions
    associated with a specific user

    Attributes
    ----------
    name : str
        Name of the user
    email : str
        Email of the user
    password : str
        Password of the user
    tasks : str
        Tasks associated to the user
    db_connection : str
        Database connection
    """

    def __init__(self, user: User, user_db: Dict[str, str]) -> None:
        """
        User handler constructor

        Parameters
        ----------
        user : User
            Data associated with a user
        user_db : Dict[str, str]
            Credentials to be able to interact with the database
        """

        self.name = user.name
        self.email = user.email
        self.password = user.password
        self.tasks = user.tasks
        self.db_connection = Database(**user_db).get_connection()
