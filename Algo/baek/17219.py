from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

table = {}
for _ in range(n):
    site, password = input().split()
    table[site] = password

for _ in range(m):
    print(table[input().rstrip('\n')])