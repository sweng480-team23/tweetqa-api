from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class CollectionDTOResponse(object):
    items: list
    length: int

    def __init__(self) -> None:
        self.items = []
        self.length = 0

    def add(self, item: T) -> None:
        self.items.append(item)
        self.length+=1

    def remove(self, item: T) -> None:
        self.items.remove(item)
        self.length-=1


