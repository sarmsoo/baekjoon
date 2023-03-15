t = int(input())
sites = []
for _ in range(t):
    n, m = map(int, input().split())
    sites.append((n, m))

for n, m in sites:
    result = 1
    if n == m:
        print(result)
        continue
    else:
        for i in range(m - n + 1, m + 1):
            result = result * i
        for j in range(1, n + 1):
            result = result // j
    print(result)
