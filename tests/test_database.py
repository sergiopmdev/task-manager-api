import os
from unittest import mock

import pytest

from exceptions.database import DatabaseCredentialsError
from models.UserDB import UserDB
from utils.Database import Database, get_db_credentials


mocked_db_credentials = {
    "DB_USERNAME": "username",
    "DB_PASSWORD": "password",
    "DB_CLUSTER": "cluster",
}


def test_db_credentials():
    assert isinstance(get_db_credentials(), UserDB)


@mock.patch.dict(os.environ, clear=True)
def test_db_credentials_validation_error():
    with pytest.raises(DatabaseCredentialsError):
        get_db_credentials()


@mock.patch.dict(os.environ, mocked_db_credentials, clear=True)
def test_get_string_connection():
    expected_string_connection = (
        "mongodb+srv://username:password@cluster"
        ".zss0em4.mongodb.net/?retryWrites=true&w=majority"
    )
    assert Database()._get_string_connection() == expected_string_connection
