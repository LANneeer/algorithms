class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vals = {}
        for i in range(len(nums)):
            if target - nums[i] in vals:
                return [vals[target - nums[i]], i]
            else:
                vals[nums[i]] = i

    def tests(self):
        assert self.twoSum([2, 7, 11, 15], 9) == [0, 1], self.twoSum([2, 7, 11, 15], 9)
        assert self.twoSum([3, 2, 4], 6) == [1, 2], self.twoSum([3, 2, 4], 6)
        assert self.twoSum([3, 3], 6) == [0, 1], self.twoSum([3, 3], 6)
        print("everything allright")


if __name__ == "__main__":
    Solution().tests()
