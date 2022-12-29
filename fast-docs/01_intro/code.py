from typing import Optional


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


# print(get_full_name("john", "doe"))
# print(get_name_with_age('Hung', 31))

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):    # Simple types
    return item_a, item_b, item_c, item_d, item_d, item_e


# Generic types
def process_items(items: list[str]):
    for item in items:
        print(item)


def pprocess_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def prrocess_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)


# Union
def process_item(item: int | str):
    print(item)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# 3.10 Optional: using vertical bar |
def say_hi_10(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# def say_hi(name: str | None):
#     print(f"Hey {name}!")


# process_items(items=[1, 2, 3, 4, 5])


# Class
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person) -> str:
    return one_person.name
