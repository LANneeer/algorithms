from collections import deque


class Stack:
    """
    Stack is a data structure which uses array as a stack,
    stack uses FILO concept (First In Last Out)
    """
    def __init__(self):
        self.items = deque()

    def __repr__(self):
        return f'{self.items}'

    def __iter__(self):
        while self.items:
            yield self.peek()

    def push(self, item) -> None:
        self.items.append(item)

    def peek(self) -> object:
        return self.items.pop()

