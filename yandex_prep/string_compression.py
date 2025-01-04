def compress(arr: list[str]) -> int:
    i = 0
    j = 0
    while i < len(arr):
        count = 0
        while j + 1 < len(arr) and arr[i] == arr[j + 1]:
            j += 1
            count += 1
        arr[i] = arr[j]
        i += 1
        if count > 1:
            for c in str(j - i):
                arr[i] = arr[c]
                i += 1
        j = j + 1


if __name__ == "__main__":
    # Тест 1: Повторяющиеся символы
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert compress(chars) == 6
    assert chars[:6] == ["a", "2", "b", "2", "c", "3"], f"Test 1 failed: {chars}"

    # Тест 2: Один символ
    chars = ["a"]
    assert compress(chars) == 1
    assert chars[:1] == ["a"], f"Test 2 failed: {chars}"

    # Тест 3: Много повторений
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert compress(chars) == 4
    assert chars[:4] == ["a", "b", "1", "2"], f"Test 3 failed: {chars}"

    # Тест 4: Разные символы
    chars = ["a", "b", "c"]
    assert compress(chars) == 3
    assert chars[:3] == ["a", "b", "c"], f"Test 4 failed: {chars}"

    # Тест 5: Все одинаковые символы
    chars = ["a", "a", "a", "a", "a"]
    assert compress(chars) == 2
    assert chars[:2] == ["a", "5"], f"Test 5 failed: {chars}"

    print("All tests passed!")
