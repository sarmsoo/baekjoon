from sys import stdin
input = stdin.readline

def sol(cnt, start):
    if cnt == 6:
        print(*result)
        return

    for i in range(start, k):
        result.append(num[i])

        sol(cnt + 1, i + 1)

        result.pop()

while True:
    k, *num = map(int, input().split())
    if k == 0:
        break
    result = []
    sol(0, 0)
    print()
