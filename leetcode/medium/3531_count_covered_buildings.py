from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_min = [n + 1] * (n + 1)  # [ y1 y2 y3 y4 ]
        x_max = [0] * (n + 1)  # [ y1 y2 y3 y4 ]
        y_min = [n + 1] * (n + 1)  # [ x1 x2 x3 x4 ]
        y_max = [0] * (n + 1)  # [ x1 x2 x3 x4 ]
        for x, y in buildings:
            x_min[x] = min(x_min[x], y)
            x_max[x] = max(x_max[x], y)
            y_min[y] = min(y_min[y], x)
            y_max[y] = max(y_max[y], x)
        # Xmin < Y < Xmax - is covered by Ox
        # Ymin < X < Ymax - is covered by Oy
        covered = 0
        for x, y in buildings:
            if x_min[x] < y < x_max[x] and y_min[y] < x < y_max[y]:
                covered += 1
        return covered


if __name__ == "__main__":
    test1 = Solution().countCoveredBuildings(
        n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
    )
    assert test1 == 1, test1
    test2 = Solution().countCoveredBuildings(
        n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]
    )
    assert test2 == 0, test2
    test3 = Solution().countCoveredBuildings(
        n=5, buildings=[[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
    )
    assert test3 == 1, test3
