t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    maximal = max(a)
    print(a.count(maximal))
    t -= 1
