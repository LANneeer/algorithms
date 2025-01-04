def summaryRanges(nums: list[int]) -> list[str]:
    i = 0
    j = 0
    output = []
    while i < len(nums):
        while j + 1 < len(nums) and nums[j + 1] - nums[j] == 1:
            j += 1
        if j - i >= 1:
            output.append("{}->{}".format(nums[i], nums[j]))
        else:
            output.append("{}".format(nums[i]))
        i = j + 1
        j = j + 1
    return output


if __name__ == "__main__":
    # Тест 1: Стандартный случай
    nums = [0, 1, 2, 4, 5, 7]
    assert summaryRanges(nums) == [
        "0->2",
        "4->5",
        "7",
    ], f"Test 1 failed: {summaryRanges(nums)}"

    # Тест 2: Разрывы в последовательности
    nums = [0, 2, 3, 4, 6, 8, 9]
    assert summaryRanges(nums) == [
        "0",
        "2->4",
        "6",
        "8->9",
    ], f"Test 2 failed: {summaryRanges(nums)}"

    # Тест 3: Пустой список
    nums = []
    assert summaryRanges(nums) == [], f"Test 3 failed: {summaryRanges(nums)}"

    # Тест 4: Один элемент
    nums = [1]
    assert summaryRanges(nums) == ["1"], f"Test 4 failed: {summaryRanges(nums)}"

    # Тест 5: Все числа подряд
    nums = [1, 2, 3, 4, 5]
    assert summaryRanges(nums) == ["1->5"], f"Test 5 failed: {summaryRanges(nums)}"

    print("All tests passed!")
