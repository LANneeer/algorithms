from random import randint


def find_max_diff(prices: list, start: int, end: int) -> tuple[int, int, int]:
    if start >= end:
        return 0, start, end

    mid = (start + end) // 2
    left_diff, left_buy, left_sell = find_max_diff(prices, start, mid)
    right_diff, right_buy, right_sell = find_max_diff(prices, mid + 1, end)

    min_price_left = min(prices[start:mid+1])
    max_price_right = max(prices[mid+1:end+1])
    cross_diff = max_price_right - min_price_left

    min_price_left_index = prices[start:mid+1].index(min_price_left) + start
    max_price_right_index = prices[mid+1:end+1].index(max_price_right) + mid + 1

    if cross_diff > left_diff and cross_diff > right_diff:
        return cross_diff, min_price_left_index, max_price_right_index
    elif left_diff > right_diff:
        return left_diff, left_buy, left_sell
    else:
        return right_diff, right_buy, right_sell


prices = [randint(1, 999) for i in range(10)]
max_diff, buy_day, sell_day = find_max_diff(prices, 0, len(prices)-1)
print(prices)
print(f"max profit: {max_diff} - buy at: {buy_day} - sell at: {sell_day}")

