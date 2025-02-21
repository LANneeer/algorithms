def max_sub_array(arr: list, k: int) -> int:
    pref_sum = sum(arr[:k])
    max_sum = pref_sum
    for i in range(k, len(arr)):
        pref_sum = arr[i] + pref_sum - arr[i - k]
        max_sum = max(max_sum, pref_sum)
    return max_sum


# if __name__ == "__main__":
#     resp = max_sub_array([1, 2, 3, 4, 5, 6], 3)
#     assert resp == 15, resp
#     resp = max_sub_array([6, 5, 4, 3, 2, 1], 3)
#     assert resp == 15, resp
#     resp = max_sub_array([0, 0, 1, 0, 0, 1], 3)
#     assert resp == 1, resp
#     resp = max_sub_array([0], 1)
#     assert resp == 0, resp


def compress_ranges(arr: list) -> list:
    length = len(arr)
    i = 0
    j = 1
    new_arr = []
    while i < length:
        while j < length and arr[j] - arr[j - 1] == 1:
            j += 1
        if j - i > 1:
            new_arr.append("{}->{}".format(arr[i], arr[j - 1]))
        else:
            new_arr.append("{}".format(arr[i]))
        i = j
        j += 1

    return new_arr


# if __name__ == "__main__":
#     resp = compress_ranges([0, 1, 2, 4, 5, 6, 10, 11])
#     assert resp == ["0->2", "4->6", "10->11"], resp
#     resp = compress_ranges([8, 7, 6, 5, 4, 1, 2, 3])
#     assert resp == ["8", "7", "6", "5", "4", "1->3"], resp
#     resp = compress_ranges([0, 1])
#     assert resp == ["0->1"], resp
#     resp = compress_ranges([1])
#     assert resp == ["1"], resp
#


def max_sub_text(s: str) -> int:
    if len(s) < 1:
        return -1
    uniques = set()
    max_count = count = 0
    for _ in range(len(s)):
        for i in s:
            if i not in uniques:
                count += 1
                uniques.add(i)
            else:
                if max_count < count:
                    max_count = count
                count = 0
                uniques.clear()
    return max_count


if __name__ == "__main__":
    resp = max_sub_text("abbcd")
    assert resp == 3, resp


def fake_report(arr: list, k: int) -> int:
    length = len(arr)
    if k > length or length < 1:
        return k
    max_count = count = 0
    fake_applyied = 0
    for _ in range(length):
        for i in arr:
            if i == 1:
                count += 1
            elif i == 0 and fake_applyied < k:
                count += 1
                fake_applyied += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0
                fake_applyied = 0
                break
    return max_count


def max_sub_mul_array(arr: list, k: int) -> int:
    zeros = 0
    max_mul = mul = 1
    length = len(arr)
    if k > length or length < 2:
        return k
    for i in arr[:k]:
        if i == 0:
            zeros += 1
        else:
            mul *= i
    if zeros > 0:
        max_mul = 0
    else:
        max_mul = mul
    for i in range(k, len(arr)):
        if i == 0:
            zeros += 1
        else:
            mul = arr[i - k] / mul * arr[i]
        if zeros == 0:
            max_mul = mul
        zeros = 0


# if __name__ == "__main__":
# arr = [1, 2, 3, 5, 6, 9]
# k = 3
# print(max_sub_array(arr, k))
# my_range = [1, 2, 3, 4, 5, 8, 10, 15, 16, 20, 21, 22]
# print(compress_ranges(my_range))
# print(max_sub_text("yxyabcdefgx"))
# print(fake_report([1, 0, 1, 1, 0, 1, 1, 0], 1))
