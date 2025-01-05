# 1
a = 7 + 3 * 6 / 2 - 1
b = 3 * 9 * (3 + (4 * 5 / 3))
c = 12.0 + 2 / 5 * 10.0
d = 2 / 5 + 10.0 * 3 - 2.5

print(a, b, c, d)


# 2
def fohrenhaits_to_celsium(F: float) -> float:
    return (5 / 9) * (F - 32)


print(fohrenhaits_to_celsium(100.10))


# 3
def circle_info(R: float) -> tuple[float, float, float]:
    return R * 2, 2 * (22 / 7) * R, (22 / 7) * (R**2)


print(circle_info(10.5))


# 4
def calculate_info(a_point: tuple[int, int], b_point: tuple[int, int]) -> float:
    return ((b_point[0] - a_point[0]) ** 2 + (b_point[1] - a_point[1]) ** 2) ** 0.5


print(calculate_info((1, 2), (3, 6)))


# 5
def stftime(seconds: int) -> str:
    H = seconds // 3600
    M = (seconds % 3600) // 60
    S = (seconds % 3600) % 60
    return f"H: {H} M: {M} S: {S}"


print(stftime(5142))


# 6
def change(cents: int, item_cost: int) -> str:
    s = ""
    change_rate = cents - item_cost
    for i in [50, 20, 10, 5, 2, 1]:
        if change_rate // i != 0:
            s += f"Number of {i} cent coins : {change_rate // i}\n"
        change_rate %= i
    return s


print(change(100, 45))
