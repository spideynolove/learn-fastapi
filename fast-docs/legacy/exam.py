from modul.types_intro import add, get_full_name
from modul.class_intro import *
from modul.pydactic_intro import *

# -------------------------------------------------
add(1, 2)
get_full_name("john", "doe")

# -------------------------------------------------
person = Person("Hung")
name = get_person_name(1, person)
print(name)

# -------------------------------------------------
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)