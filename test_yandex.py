class ZigZag:
    def __init__(self, *args):
        self.cur = 0
        self.size = len(args)
        self.indexes = [0] * self.size
        self.vectors = [*args]

    def next(self) -> int:
        vector = self.vectors[self.cur]
        index = self.indexes[self.cur]

        result = vector[index]
        self.indexes[self.cur] = index + 1
        self.cur = (self.cur + 1) % self.size
        return result

    def hasNext(self) -> bool:
        start = self.cur
        while self.indexes[self.cur] == len(self.vectors[self.cur]):
            self.cur = (self.cur + 1) % self.size
            if self.cur == start:
                return False
        return True


iterator = ZigZag([1, 2, 3, 4], [5, 6, 7, 8])
new = []
while iterator.hasNext():
    new.append(iterator.next())

print(new)
