from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = arr[:]
answer = 0

for i in range(1, n):
    s[i] += s[i - 1]

for i in range(1, n - 1):
    answer = max(answer, 2 * s[-1] - arr[-1] - arr[i] - s[i])

for i in range(1, n - 1):
    answer = max(answer, s[-1] - arr[-1] - arr[i] + s[i - 1])

for i in range(1, n - 1):
    answer = max(answer, s[i] - arr[0] + s[-1] - s[i - 1] - arr[-1])

print(answer)