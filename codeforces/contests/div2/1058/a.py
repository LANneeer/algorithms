def diffel(n: int, b: list) -> list:
    d = [0] * (n + 1)
    d[1] = b[0]
    for i in range(2, n + 1):
        d[i] = b[i - 1] - b[i - 2]

    a = [0] * (n + 1)
    next_label = 0
    for i in range(1, n + 1):
        p = i - d[i]
        if p == 0:
            next_label += 1
            a[i] = next_label
        else:
            a[i] = a[p]
    return a[1:]
q = int(input())
for _ in range(q):
    print(*diffel(int(input()), list(map(int, input().split()))))

