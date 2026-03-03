def sorter(length: int, arr: list[int]) -> str:
    back = arr[0]
    front = arr[0]
    for ptr in range(1, length):
        if ptr * 2 >= length:
            if arr[ptr] < back:
                return "NO"
            else:
                while ptr + 1 < length:
                    if arr[ptr] > arr[ptr + 1]:
                        return "NO"
                    ptr += 1
                return "YES"
        back = min(arr[ptr - 1], arr[(ptr * 2) - 1])
        front = min(arr[ptr], arr[ptr * 2])
        if front < back:
            return "NO"
    return "YES"


for _ in range(int(input())):
    print(sorter(length=int(input()), arr=list(map(int, input().split()))))
