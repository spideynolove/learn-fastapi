from datetime import datetime
from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []