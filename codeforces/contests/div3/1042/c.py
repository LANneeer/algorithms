def equality(t: int) -> None:
    for _ in range(t):
        n, k = map(int, input().split())
        S = list(map(int, input().split()))
        T = list(map(int, input().split()))
        for i in range(n):
            print("i = ", i, (((S[i] + T[i]) % k) % 2) == ((S[i] + T[i]) % 2 ))

        print("===============")

equality(int(input()))
