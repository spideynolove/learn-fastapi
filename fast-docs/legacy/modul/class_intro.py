class Person:
    def __init__(self, name: str) -> None:
        self.name = name


def get_person_name(age: int, one_person: Person) -> str:
    return f"{one_person.name} is {age} year olds"