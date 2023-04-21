from sys import stdin
input = stdin.readline

n = int(input())
prev = 20001
answer = 0
table = []
for _ in range(n):
    table.append(int(input()))

for i in range(n - 1, -1, -1):
    curr = table[i]
    if curr >= prev:
        answer += curr - prev + 1
        prev = prev - 1
    else:
        prev = curr

print(answer)