from sys import stdin
input = stdin.readline

def change(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] = '0' if A[i][j] == '1' else '1'

def check():
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True

n, m = map(int, input().split())
A = [list(input().strip()) for _ in range(n)]
B = [list(input().strip()) for _ in range(n)]

answer = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            change(i, j)
            answer += 1

if check():
    print(answer)
else:
    print(-1)