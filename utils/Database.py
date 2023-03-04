import os

from dotenv import load_dotenv
from pydantic import ValidationError
from pymongo import MongoClient

from exceptions.database import DatabaseCredentialsError
from models.UserDB import UserDB


load_dotenv()


def get_db_credentials() -> UserDB:
    """
    Extract the credentials to connect to the database
    from the environment variables defined in the .env file

    Returns
    -------
    UserDB
        Credentials of a user with access to the database

    Raises
    ------
    DatabaseCredentialsError
        Exception raised when there has been
        an error obtaining database credentials
    """

    try:
        return UserDB(
            username=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            cluster=os.getenv("DB_CLUSTER"),
        )
    except ValidationError:
        error = "Error with database credentials. Check the .env file"
        raise DatabaseCredentialsError(error)


class Database:
    """
    MongoDB client generator

    Attributes
    ----------
    username : str
        Database username
    password : str
        Password associated to the username
    cluster : str
        Cluster of the database to be accessed
    """

    def __init__(self, username: str, password: str, cluster: str) -> None:
        """
        MongoDB client generator constructor

        Parameters
        ----------
        username : str
            Database username
        password : str
            Password associated to the username
        cluster : str
            Cluster of the database to be accessed
        """

        self._username = username
        self._password = password
        self._cluster = cluster

    def _get_string_connection(self) -> str:
        """
        Generate connection string from the obtained set of credentials

        Returns
        -------
        str
            Connection string
        """

        return (
            f"mongodb+srv://{self._username}:{self._password}@{self._cluster}"
            ".zss0em4.mongodb.net/?retryWrites=true&w=majority"
        )

    def get_connection(self) -> MongoClient:
        """
        Generate database connection via generated connection string

        Returns
        -------
        MongoClient
            Database connection
        """

        return MongoClient(self._get_string_connection())
