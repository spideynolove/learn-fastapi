from typing import Union, Optional


def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def add(a: int, b: int) -> int:
    return a + b


def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items_ts(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items_d(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# def say_hi(name: Optional[str] = None):
#     print(f"Hey {name}!") if name is not None else print("Hello World")


def say_h_ui(name: Union[str, None] = None):    
    '''prefer than Optional'''
    print(f"Hey {name}!") if name is not None else print("Hello World")


def process_item_u(item: Union[int, str]):
    print(item)
