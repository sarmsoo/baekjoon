from sys import stdin
input = stdin.readline

def sol():
    answer = 0
    for i in range(1 << n * m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0:
                    rowsum = rowsum * 10 + graph[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        for col in range(m):
            colsum = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    colsum = colsum * 10 + graph[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum

        answer = max(answer, total)
    return answer


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

print(sol())