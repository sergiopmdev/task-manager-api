from pydantic import BaseModel


class UserDB(BaseModel):
    username: str
    password: str
    cluster: str
