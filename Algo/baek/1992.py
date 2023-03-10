from sys import stdin
input = stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

result = []


def sol(n, y, x, r):
    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[y][x] != graph[i][j]:
                result.append('(')
                sol(n // 2, y, x, 1)
                sol(n // 2, y, x + n // 2, 2)
                sol(n // 2, y + n // 2, x, 3)
                sol(n // 2, y + n // 2, x + n // 2, 4)
                result.append(')')
                return

    if graph[y][x] == '1':
        result.append('1')
    else:
        result.append('0')


sol(n, 0, 0, 0)
print(''.join(result))

