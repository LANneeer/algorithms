from typing import List


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def build(k: int) -> List[List[int]]:
            if k == 0:
                return [[0]]

            small = build(k - 1)
            s = len(small)
            block = s * s
            size = s * 2
            res = [[0] * size for _ in range(size)]

            for i in range(s):
                for j in range(s):
                    v = small[i][j]
                    res[i][j + s] = v
                    res[i + s][j + s] = v + block
                    res[i + s][j] = v + 2 * block
                    res[i][j] = v + 3 * block
            return res

        return build(N)


if __name__ == "__main__":
    test1 = Solution().specialGrid(0)
    assert test1 == [[0]], test1

    test2 = Solution().specialGrid(1)
    assert test2 == [[3, 0], [2, 1]], test2

    test3 = Solution().specialGrid(2)
    assert test3 == [[15, 12, 3, 0], [14, 13, 2, 1], [11, 8, 7, 4], [10, 9, 6, 5]], (
        test3
    )
