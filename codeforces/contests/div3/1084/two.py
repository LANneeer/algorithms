t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    for i in range(n):
        if a[i] != b[i]:
            print(1)
            break
    else:
        print(n)
    t -= 1
