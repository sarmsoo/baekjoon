from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
d, b = set(), set()

for _ in range(n):
    d.add(input().strip())
for _ in range(m):
    b.add(input().strip())

db = list(d & b)
print(len(db))
db.sort()
for name in db:
    print(name)