def gen_seq(t: int) -> None:
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            if i % 2 == 0:
                arr.append(-1)
            else:
                if i >= n - 1:
                    arr.append(2)
                else:
                    arr.append(3)
        print(*arr)

gen_seq(int(input()))
