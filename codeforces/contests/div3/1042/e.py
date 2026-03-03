import sys

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []

    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        b = [int(next(it)) for _ in range(n)]

        ok = True

        # a[n-1] cannot be changed by any operation
        if a[-1] != b[-1]:
            out.append("NO")
            continue

        # Decide from right to left
        for i in range(n - 2, -1, -1):
            if a[i] == b[i]:
                continue
            # We may apply the operation at i at most once, using the finalized a[i+1]
            if (a[i] ^ a[i + 1]) == b[i]:
                a[i] ^= a[i + 1]
            else:
                ok = False
                break

        out.append("YES" if ok else "NO")

    print("\n".join(out))

if __name__ == "__main__":
    solve()
