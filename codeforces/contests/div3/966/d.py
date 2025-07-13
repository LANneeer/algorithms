def find_most_lr(length: int, nums: list[int], comb: list[str]) -> int:
    pref_sum = l = r = 0
    while r < length:
        while l < length and comb[l] != "L":
            l += 1
        while r < length and comb[r] != "R":
            r += 1
            l = r
        pref_sum += sum(nums[l:r])

    return pref_sum


t = int(input())
while t != 0:
    print(
        find_most_lr(
            length=int(input()),
            nums=list(map(int, input().split())),
            comb=input().split(),
        )
    )
    t -= 1
