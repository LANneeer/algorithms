A = int(input())
B = int(input())
C = int(input())
D = int(input())

min_total = 0
M = 0
N = 0

if A != 0 and C != 0:
    total_blue = B + D
    if total_blue < min_total or min_total == 0:
        min_total = total_blue
        M = B + 1
        N = D + 1

if B != 0 and D != 0:
    total_red = A + C
    if total_red < min_total or min_total == 0:
        min_total = total_red
        M = A + 1
        N = C + 1

print(M, N)
