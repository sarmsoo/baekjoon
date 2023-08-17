from sys import stdin
input = stdin.readline

n = int(input())
arr = []
total = 0
for _ in range(n):
    x, a = map(int, input().split())
    arr.append((x, a))
    total -= a

arr.sort()
answer = 0
for x, a in arr:
    total += 2 * a
    if total >= 0:
        answer = x
        break

print(answer)