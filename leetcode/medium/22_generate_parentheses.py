from typing import List
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perms, queue = [], deque([(0, 0, "")])
        while queue:
            L, R, perm = queue.pop()
            if L == R == n:
                perms.append(perm)
                continue
            if L < n:
                queue.append((L + 1, R, perm + "("))
            if R < L:
                queue.append((L, R + 1, perm + ")"))
        return perms


if __name__ == "__main__":
    test1 = Solution().generateParenthesis(3)
    assert test1 == ["((()))", "(()())", "(())()", "()(())", "()()()"], test1
    test2 = Solution().generateParenthesis(1)
    assert test2 == ["()"], test2
    test3 = Solution().generateParenthesis(4)
    assert test3 == [], test3
