from pydantic import BaseModel, ValidationError
from typing import List, Optional
from datetime import datetime
msg = """ 
    - Data validation, settings management
    - type annotations, type hints at runtime
    - https://www.redhat.com/architect/12-factor-app
"""


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

# user = User(**external_data)
# print(user.id)
# print(repr(user.signup_ts))
# print(user.friends)
# print(user.dict())


try:
    User(signup_ts='broken', friends=[1, 2, 'not number'])
except ValidationError as e:
    print(e.json())

