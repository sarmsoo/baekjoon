n, m = map(int, input().split())

table = [[0] * (i + 1) for i in range(1, n + 1)]
for i in range(0, n):
    table[i][0] = 1
    table[i][-1] = 1

for i in range(0, n):
    for j in range(1, i + 1):
        table[i][j] = table[i - 1][j] + table[i - 1][j - 1]

print(table[n - 1][m])