
from abc import ABC, abstractmethod

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('_name')

    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        instance.__dict__['_name'] = value

class Person(ABC):
    name = NameDescriptor()

    def __init__(self, name: str, person_id: int):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name} (ID: {self.person_id})"

    def __eq__(self, other):
        return isinstance(other, Person) and self.person_id == other.person_id
