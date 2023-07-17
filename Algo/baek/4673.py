from sys import stdin
input = stdin.readline

result = [False] * 10001
for i in range(1, 10000):
    tmp = 0
    for j in str(i):
        tmp += int(j)

    self = i + tmp
    if self > 10000:
        break
    result[self] = True

for i in range(1, 10001):
    if not result[i]:
        print(i)