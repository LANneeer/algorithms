from abc import ABC, abstractclassmethod


class ContentBuilder(ABC):
    @abstractclassmethod
    def create_content(self, text: str, img: str) -> ContentBlock:
        raise NotImplementedError
