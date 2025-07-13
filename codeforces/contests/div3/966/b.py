def valid_seat(n: int, a: list[int]) -> str:
    left = a[0] - 1
    right = a[0] + 1
    for i in a[1:]:
        if i == left:
            left -= 1
            continue
        if i == right:
            right += 1
            continue
        if i != right and i != left:
            return "NO"
    return "YES"


t = int(input())
while t != 0:
    print(valid_seat(n=int(input()), a=list(map(int, input().split()))))
    t -= 1
