def dice(size: int, arr: list[int]) -> int:
    count = 0
    for i in range(1, size, 2):
        if arr[i - 1] + arr[i] == 7 or arr[i - 1] == arr[i]:
            count += 1
    return count


for _ in range(int(input())):
    print(dice(size=int(input()), arr=list(map(int, input().split()))))
