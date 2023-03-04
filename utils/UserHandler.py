from typing import Any, Dict, Union

from pymongo.collection import Collection

from messages.users import users_messages
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
    tasks : List[Dict[str, Any]]
        Tasks associated to the user
    db_connection : MongoClient
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

    def _check_user_exists(
        self, collection: Collection[User], email: str
    ) -> Union[Dict[str, Any], None]:
        """
        Check for the existence of a user in the database

        Parameters
        ----------
        collection : Collection[User]
            Collection of users
        email : str
            User document field by means of which
            the user search is to be performed

        Returns
        -------
        Union[Dict[str, Any], None]
            The searched user in case it exists
            or None in case it doesn't exist
        """

        return collection.find_one({"email": email})

    def create_user(self) -> str:
        """
        Insert a new user in database

        Returns
        -------
        str
            Message with the status of the insertion
        """

        users_db = self.db_connection["users_db"]
        users_collection = users_db["users_collection"]

        user = {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "tasks": self.tasks,
        }

        if self._check_user_exists(users_collection, user["email"]) is not None:
            return users_messages["user_exists"]

        inserted_user = users_collection.insert_one(user)

        return users_messages["user_created"].format(inserted_user.inserted_id)
