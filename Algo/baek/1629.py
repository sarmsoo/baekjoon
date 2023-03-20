a, b, c = map(int, input().split())

def sol(n):
    if n == 1:
        return a % c
    else:
        tmp = sol(n // 2)
        # 나머지 분배 법칙
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

def sol2(n):
    if n == 1:
        return a % c

    tmp = sol(n // 2)
    return ((tmp % c) * (tmp % c) * ((a ** (n % 2)) % c)) % c # 나머지 분배법칙

print(sol(b))
print(sol2(b))