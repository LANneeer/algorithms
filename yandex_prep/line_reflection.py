def isReflected(points: list[list[int, int], list[int, int]]) -> bool:
    x_vals = [x for x, y in points]
    xmax = max(x_vals)
    xmin = min(x_vals)
    reflection_line = xmax + xmin
    visited = set()
    for x, y in points:
        visited.add((x, y))
    for x, y in visited:
        if (reflection_line - x, y) not in visited:
            return False
    return True


if __name__ == "__main__":
    # Тест 1: Симметрия есть
    points = [[1, 1], [-1, 1]]
    assert isReflected(points) == True, f"Test 1 failed: {isReflected(points)}"

    # Тест 2: Симметрии нет
    points = [[1, 1], [-1, -1]]
    assert isReflected(points) == False, f"Test 2 failed: {isReflected(points)}"

    # Тест 3: Пустой список
    points = [[1, 0], [-1, 0], [2, 1]]
    assert isReflected(points) == False, f"Test 3 failed: {isReflected(points)}"

    # Тест 4: Все точки на одной линии
    points = [[1, 0], [-1, 0], [0, 0]]
    assert isReflected(points) == True, f"Test 4 failed: {isReflected(points)}"

    # Тест 5: Нет симметрии
    points = [[1, 1], [2, 2]]
    assert isReflected(points) == False, f"Test 5 failed: {isReflected(points)}"

    print("All tests passed!")
