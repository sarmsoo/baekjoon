from sys import stdin
input = stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

m_one = 0
zero = 0
one = 0


def sol(n, y, x):
    global one, m_one, zero

    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[y][x] != graph[i][j]:
                sol(n // 3, y, x)
                sol(n // 3, y, x + n // 3)
                sol(n // 3, y, x + 2 * n // 3)
                sol(n // 3, y + n // 3, x)
                sol(n // 3, y + n // 3, x + n // 3)
                sol(n // 3, y + n // 3, x + 2 * n // 3)
                sol(n // 3, y + 2 * n // 3, x)
                sol(n // 3, y + 2 * n // 3, x + n // 3)
                sol(n // 3, y + 2 * n // 3, x + 2 * n // 3)
                return
    if graph[y][x] == 0:
        zero += 1
    elif graph[y][x] == 1:
        one += 1
    else:
        m_one += 1
    return


sol(n, 0, 0)
print(m_one, zero, one, sep='\n')