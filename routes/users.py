from fastapi import APIRouter

from models.User import User
from utils.Database import get_db_credentials
from utils.UserHandler import UserHandler


users = APIRouter()


@users.post("/users")
def create_user(user: User):
    db_credentials = dict(get_db_credentials())
    user_handler = UserHandler(user=user, user_db=db_credentials)
    new_user = user_handler.create_user()
    return {"user_id": str(new_user.inserted_id)}
