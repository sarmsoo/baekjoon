from sys import stdin
input = stdin.readline

def sol(t):
    if t == S:
        print(1)
        exit(0)

    if len(t) == 0:
        return

    if t[-1] == 'A':
        sol(t[:-1])
    if t[0] == 'B':
        sol(t[1:][::-1])


S = input().strip()
T = input().strip()

sol(T)
print(0)