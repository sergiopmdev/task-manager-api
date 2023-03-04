from fastapi import APIRouter, HTTPException

from messages.users import users_messages
from models.User import User
from utils.Database import get_db_credentials
from utils.UserHandler import UserHandler


users = APIRouter()


@users.post("/users", status_code=201)
def create_user(user: User):
    db_credentials = dict(get_db_credentials())
    user_handler = UserHandler(user=user, user_db=db_credentials)

    user_status = user_handler.create_user()

    if user_status == users_messages["user_exists"]:
        return HTTPException(status_code=409, detail=user_status)

    return {"status": user_status}
