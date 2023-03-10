n, r, c = map(int, input().split())

def sol(n, r, c, s):
    size = 2 ** (n - 1)
    count = 4 ** (n - 1)

    if n == 0:
        return s

    if r < size:
        # 2사분면
        if c < size:
            return sol(n - 1, r, c, s + 0)
        # 1사분면
        else:
            return sol(n - 1, r, c - size, s + count)
    else:
        # 3사분면
        if c < size:
            return sol(n - 1, r - size, c, s + count * 2)
        # 4사분면
        else:
            return sol(n - 1, r - size, c - size, s + count * 3)

print(sol(n, r, c, 0))
