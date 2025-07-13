from abc import ABC, abstractclassmethod

class PageBuilder(ABC):
    @abstractclassmethod
    def create_page(self, page_number: int, contentblock: ContentBlock, max_length: int) -> Page:
        raise NotImplementedError
