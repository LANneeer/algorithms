def min_rotation(a):
    n = len(a)
    if n == 0:
        return a

    s = a + a
    i, j, offset = 0, 1, 0

    while i < n and j < n and offset < n:
        if s[i + offset] == s[j + offset]:
            offset += 1
            continue
        if s[i + offset] > s[j + offset]:
            i = i + offset + 1
            if i == j:
                i += 1
        else:
            j = j + offset + 1
            if i == j:
                j += 1
        offset = 0

    start = min(i, j)
    return s[start : start + n]


t = int(input())
while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    inner = a[x:y]
    outer = a[:x] + a[y:]

    inner = min_rotation(inner)
    outer = min_rotation(outer)
    result = outer[:x] + inner + outer[x:]

    print(*result)
    t -= 1
