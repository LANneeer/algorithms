class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        num_ranges = []
        i = j = 0
        while i < len(nums):
            while j + 1 < len(nums) and nums[j] + 1 == nums[j + 1]:
                j += 1
            if j - i >= 1:
                str_output = f"{nums[i]}->{nums[j]}"
            else:
                str_output = f"{nums[i]}"
            num_ranges.append(str_output)
            i = j + 1
            j = j + 1
        return num_ranges

