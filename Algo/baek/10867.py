from sys import stdin
input = stdin.readline

n = int(input())
data = list(map(int, input().split()))
data = list(set(data))
data.sort()
print(*data)