from fastapi import APIRouter
from exceptions.users import UserAlreadyExists

from messages.users import users_messages
from models.User import User
from utils.UserHandler import UserHandler


users = APIRouter()


@users.post("/users", status_code=201)
def create_user(user: User):
    user_handler = UserHandler(user=user)

    user_status = user_handler.create_user()

    if user_status == users_messages["user_exists"]:
        raise UserAlreadyExists(status_code=409, detail=user_status)
    return {"status": user_status}
