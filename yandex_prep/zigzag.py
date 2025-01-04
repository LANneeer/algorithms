class ZigzagIterator:
    def __init__(self, vectors1, vectors2):
        self.vectors = [vectors1, vectors2]
        self.turn = 0
        self.pointers = [0, 0]

    def next(self):
        while self.pointers[self.turn] >= len(self.vectors[self.turn]):
            self.turn = (self.turn + 1) % 2
        result = self.vectors[self.turn][self.pointers[self.turn]]
        self.pointers[self.turn] += 1
        self.turn = (self.turn + 1) % 2
        return result

    def hasNext(self):
        return any(self.pointers[i] < len(self.vectors[i]) for i in range(2))


if __name__ == "__main__":
    # Тест 1: Обычный случай
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    zigzag = ZigzagIterator(v1, v2)
    assert zigzag.next() == 1
    assert zigzag.next() == 3
    assert zigzag.next() == 2
    assert zigzag.next() == 4
    assert zigzag.next() == 5
    assert zigzag.next() == 6
    assert zigzag.hasNext() == False

    # Тест 2: Один список пустой
    v1 = []
    v2 = [3, 4, 5]
    zigzag = ZigzagIterator(v1, v2)
    assert zigzag.next() == 3
    assert zigzag.next() == 4
    assert zigzag.next() == 5
    assert zigzag.hasNext() == False

    # Тест 3: Оба списка пустые
    v1 = []
    v2 = []
    zigzag = ZigzagIterator(v1, v2)
    assert zigzag.hasNext() == False

    # Тест 4: Одинаковые размеры списков
    v1 = [1, 3, 5]
    v2 = [2, 4, 6]
    zigzag = ZigzagIterator(v1, v2)
    result = [zigzag.next() for _ in range(6)]
    assert result == [1, 2, 3, 4, 5, 6], f"Test 4 failed: {result}"

    print("All tests passed!")
