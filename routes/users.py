from fastapi import APIRouter

from models.User import User


users = APIRouter()


@users.post("/users")
def create_user(user: User):
    return {"user": user}
