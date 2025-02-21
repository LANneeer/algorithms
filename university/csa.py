from abc import ABC, abstractmethod
from typing import Any


class Color:
    def __init__(self, c: int, m: int, y: int, k: int):
        self.c = c
        self.m = m
        self.y = y
        self.k = k


class Strategy(ABC):
    @abstractmethod
    def calculate(self, **kwargs) -> Any:
        raise NotImplementedError


class Memory:
    def __init__(self, strategy: Strategy, N: int, M: int):
        self._strategy = strategy
        self.main = self.create(N, M, (0, 0, 0, 0))
        self.cache = [None] * K

    @staticmethod
    def create(N: int, M: int, value: tuple) -> list[list[Color]]:
        return [[Color(*value) for _ in range(M)] for _ in range(N)]

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def get_info(self, **kwargs) -> dict:
        result = self._strategy.calculate(memories=(self.main, self.cache), **kwargs)
        return {
            "Access:": result["access"],
            "Hits:": result["hit"],
            "Misses:": result["miss"],
            "Hits in percent:": str(result["hit"] / result["access"] * 100) + "%",
            "Misses in percent:": str(result["miss"] / result["access"] * 100) + "%",
        }


class BaseStrategy(Strategy):
    def calculate(self, **kwargs) -> None: ...

    @staticmethod
    def find_cell(main: list[list[None]], cache: list[list[None]], i, j):
        for k in range(len(cache)):
            if cache[k] is not None and cache[k] == main[i][j]:
                return True
        return False

    @staticmethod
    def fill(main: list[list[None]], cache: list[None], i, j):
        for k in range(len(cache)):
            if j + k < len(main[i]) and cache[k] is None:
                cache[k] = main[i][j + k]


class FirstStrategy(BaseStrategy):
    def calculate(self, **kwargs) -> dict[str, int]:
        hit = 0
        miss = 0
        access = 0
        main, cache = kwargs["memories"]

        for i in range(len(main)):
            for j in range(len(main[i])):
                for k in range(4):
                    access += 1
                    if self.find_cell(main, cache, i, j):
                        hit += 1
                    else:
                        miss += 1
                        cache = [None] * len(cache)
                        self.fill(main, cache, i, j)
        return {"access": access, "hit": hit, "miss": miss}


class SecondStrategy(BaseStrategy):
    def calculate(self, **kwargs) -> dict[str, int]:
        hit = 0
        miss = 0
        access = 0
        main, cache = kwargs["memories"]

        for i in range(len(main)):
            for j in range(len(main[i])):
                for k in range(4):
                    access += 1
                    if self.find_cell(main, cache, i, j):
                        hit += 1
                    else:
                        miss += 1
                        cache = [None] * len(cache)
                        self.fill(main, cache, i, j)
        return {"access": access, "hit": hit, "miss": miss}


class ThirdStrategy(BaseStrategy):
    def calculate(self, **kwargs) -> dict[str, int]:
        hit = 0
        miss = 0
        access = 0
        main, cache = kwargs["memories"]

        for i in range(len(main)):
            for j in range(len(main[i])):
                access += 1
                if self.find_cell(main, cache, i, j):
                    hit += 1
                else:
                    miss += 1
                    cache = [None] * len(cache)
                    self.fill(main, cache, i, j)

        for i in range(len(main)):
            for j in range(len(main[i])):
                for k in range(3):
                    access += 1
                    if self.find_cell(main, cache, i, j):
                        hit += 1
                    else:
                        miss += 1
                        cache = [None] * len(cache)
                        self.fill(main, cache, i, j)
        return {"access": access, "hit": hit, "miss": miss}


if __name__ == "__main__":
    N, M = map(int, input("N, M for main: ").split())
    K = int(input("K for cache: "))
    num = int(input("Algorithm: "))
    if num == 1:
        memory = Memory(FirstStrategy(), N, M)
        info = memory.get_info()
        print(info)
    if num == 2:
        memory = Memory(SecondStrategy(), N, M)
        info = memory.get_info()
        print(info)
    if num == 3:
        memory = Memory(ThirdStrategy(), N, M)
        info = memory.get_info()
        print(info)
