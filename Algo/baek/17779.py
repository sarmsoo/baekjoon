from sys import stdin
input = stdin.readline

def sol(x, y, d1, d2):
    temp = [[0] * (n + 1) for _ in range(n + 1)]
    temp[x][y] = 5
    for i in range(1, d1 + 1):
        temp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        temp[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        temp[x + d2 + i][y + d2 - i] = 5

    count = [0] * 5
    # 1번
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if temp[r][c] == 5:
                break
            else:
                count[0] += data[r][c]
    # 2번
    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if temp[r][c] == 5:
                break
            else:
                count[1] += data[r][c]
    # 3번
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if temp[r][c] == 5:
                break
            else:
                count[2] += data[r][c]
    # 4번
    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            else:
                count[3] += data[r][c]
    # 5번
    count[4] = total - sum(count)
    return max(count) - min(count)


n = int(input())
data = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n + 1):
    total += sum(data[i])

result = int(1e9)
for x in range(1, n + 1):
    for y in range(1, n + 1):

        for d1 in range(1, n):
            if y - d1 < 1:
                break
            for d2 in range(1, n):
                if x + d1 + d2 > n:
                    break
                if y + d2 > n:
                    break

                result = min(result, sol(x, y, d1, d2))

print(result)