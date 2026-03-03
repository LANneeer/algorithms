def lever(t: int) -> None:
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        out = 1
        for i in range(n):
            if a_list[i] > b_list[i]:
                out += a_list[i] - b_list[i]
        print(out)

lever(int(input()))
        
