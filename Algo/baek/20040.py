from sys import stdin
input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    if a < b: # a > b로 바뀌면 시간초과 or recursionError 나는데 도대체 왜?
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = list(range(n))

for i in range(m):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)

    if a == b:
        print(i + 1)
        exit(0)
    union(a, b)

print(0)