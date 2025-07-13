from ..core.book import ILib
from ..core.contentblock import ContentBuilder
from ..core.page import PageBuilder
from ..models.book import Book
from ..models.contentblock import ContentBlock
from ..models.page import Page


class Lib(ILib, PageBuilder, ContentBuilder):
    def create_page(self, page_number: int, contentblock: ContentBlock, max_length: int) -> Page:
        ...
        return Page(page_number=page_number, contentblock=contentblock, max_length=max_length)

    def create_content(self, text: str, img: str) -> ContentBlock:
        ...
        return ContentBlock(text=text, img=img)

    def create_book(self, publisher, author, title, text, img) -> Book:
        contentblock = self.create_content(text=text, img=img) 
        page = self.create_page(text=text, img=img) 
        self.book = Book(publisher=publisher, author=author, title=title, content=content)
    
        return self.book

    def get_book(self) -> Book:
        return self.book

    def read_book(self, book: Book) -> str:
        return book.content


