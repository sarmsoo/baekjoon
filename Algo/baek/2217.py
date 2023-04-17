from sys import stdin
input = stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort()

max_ = 0
for i in range(n):
    max_ = max(max_, ropes[i] * (n - i))

print(max_)
