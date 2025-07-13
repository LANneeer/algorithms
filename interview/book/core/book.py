from abc import ABC, abstractclassmethod
from ..models.book import Book


class ILib(ABC):
    @abstractclassmethod
    def create_book(self, publisher: str, author: str, title: str, content: list[str]) -> Book:
        raise NotImplementedError

    @abstractclassmethod
    def read_book(self, title: str) -> Book:
        raise NotImplementedError

