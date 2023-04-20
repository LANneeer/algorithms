from collections import deque


class Queue:
    """
    Queue is a data structure which uses array as a line of queue,
    queue uses FIFO concept (First In First Out)
    """
    def __init__(self):
        self.items = deque()

    def __repr__(self):
        return f'{self.items}'

    def __iter__(self):
        while self.items:
            yield self.dequeue()

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> object:
        return self.items.popleft()
