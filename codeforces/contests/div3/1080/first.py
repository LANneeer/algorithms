def six_seven(arr: list[int]) -> str:
    if 67 in arr:
        return "YES"
    else:
        return "NO"


for i in range(int(input())):
    n = int(input())
    print(six_seven(list(map(int, input().split()))))
