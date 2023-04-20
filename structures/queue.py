from collections import deque


class Queue:
    """
    Queue is a data structure which uses array as a line of queue,
    queue uses FIFO concept (First In First Out)
    """
    def __init__(self):
        self.items = deque()

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> object:
        return self.items.popleft()
