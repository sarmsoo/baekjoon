from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())

if k >= n:
    print(0)
    exit(0)

sensors = list(map(int, input().split()))
sensors.sort()

dist = []
for i in range(n - 1):
    dist.append(sensors[i + 1] - sensors[i])

dist.sort()
for _ in range(k - 1):
    dist.pop()

print(sum(dist))