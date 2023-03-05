import os
from unittest import mock
from unittest.mock import MagicMock

import pytest
from pymongo.collection import Collection

from models.User import User
from utils.UserHandler import UserHandler


mocked_db_credentials = {
    "DB_USERNAME": "username",
    "DB_PASSWORD": "password",
    "DB_CLUSTER": "cluster",
}


@pytest.fixture
def user() -> User:
    return User(name="name", email="email", password="password")


@pytest.fixture
@mock.patch.dict(os.environ, mocked_db_credentials, clear=True)
@mock.patch("utils.UserHandler.Database.get_connection", MagicMock())
def user_handler(user: User) -> UserHandler:
    return UserHandler(user=user)


def test_user_not_exists(user_handler: UserHandler):
    mocked_collection = MagicMock(Collection)
    email = user_handler.email
    user_handler._check_user_exists(collection=mocked_collection, email=email)
    assert mocked_collection.find_one.called


def test_hash_password(user_handler: UserHandler):
    password = user_handler.password
    hashed_password = user_handler._hash_user_password(password=password)
    assert password != hashed_password


def test_create_user(user_handler: UserHandler):
    mocked_collection = user_handler.db_connection["users_db"]["users_collection"]
    mocked_find = mocked_collection.find_one
    mocked_find.return_value = None
    mocked_insert = mocked_collection.insert_one
    user_handler.create_user()
    assert mocked_insert.called
