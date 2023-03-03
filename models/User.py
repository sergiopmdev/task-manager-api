from typing import Any, Dict, List

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    tasks: List[Dict[str, Any]] = list()
