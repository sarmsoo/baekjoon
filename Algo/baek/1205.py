from sys import stdin
input = stdin.readline

n, score, p = map(int, input().split())
if n == 0:
    print(1)
    exit(0)

board = list(map(int, input().split()))

i = 0
answer = 1
if n == 0:
    print(1)
    exit(0)
while n > i:
    if score > board[i]:
        break
    elif score == board[i]:
        i += 1
    else:
        answer += 1
        i += 1
if p > i:
    print(answer)
else:
    print(-1)