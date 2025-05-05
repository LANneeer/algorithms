class Solution:
    def maxProduct(self, n: int) -> int:
        max_1 = 0
        max_2 = 0
        while n != 0:
            temp_1 = max(max_1, n % 10)
            temp_2 = max(max_2, n % 10)
            max_1 = max(temp_2, n % 10, max_1)
            n //= 10
            max_2 = max(temp_1, n % 10, max_2)
            n //= 10
        return max_1 * max_2


if __name__ == "__main__":
    test1 = Solution().maxProduct(31)
    assert test1 == 3, test1

    test2 = Solution().maxProduct(22)
    assert test2 == 4, test2

    test3 = Solution().maxProduct(324)
    assert test3 == 12, test3

    test4 = Solution().maxProduct(12345678222323)
    assert test4 == 0, test4
