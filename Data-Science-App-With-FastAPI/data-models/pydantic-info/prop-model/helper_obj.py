import pickle
from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime = None


m = User.parse_obj({'id': 123, 'name': 'James'})    # helper 1
print(m)

try:
    User.parse_obj(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)

# assumes json as no content type passed
m = User.parse_raw('{"id": 123, "name": "James"}')  # helper 2
print(m)

pickle_data = pickle.dumps({
    'id': 123,
    'name': 'James',
    'signup_ts': datetime(2017, 7, 14)
})
m = User.parse_raw(
    pickle_data, content_type='application/pickle', allow_pickle=True
)
print(m)

path = Path('data.json')
path.write_text('{"id": 123, "name": "James"}')
m = User.parse_file(path)    # helper 2
print(m)