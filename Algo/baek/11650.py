from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()
for coor in arr:
    print(*coor)