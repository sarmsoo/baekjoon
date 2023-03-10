from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    table = {}
    n = int(input())
    for _ in range(n):
        name, kind = input().split()
        table[kind] = table.get(kind, 0) + 1

    count = 1

    for key in table:
        count *= table[key] + 1
    print(count - 1)
