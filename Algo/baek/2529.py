from sys import stdin
input = stdin.readline

k = int(input())
ine = input().strip().split()
visited = [False] * 10
result = []

def inequality_is_true(symbol, l, r):
    if symbol == '<':
        return l < r
    if symbol == '>':
        return l > r

def sol(depth):
    global min_, max_

    if depth == k + 1:
        tmp = int(''.join(map(str, result)))
        min_ = min(min_, tmp)
        max_ = max(max_, tmp)
        return

    for i in range(10):
        if depth == 0:
            result.append(i)
            visited[i] = True

            sol(depth + 1)

            result.pop()
            visited[i] = False
            continue

        if visited[i]:
            continue

        if inequality_is_true(ine[depth - 1], result[depth - 1], i):
            result.append(i)
            visited[i] = True

            sol(depth + 1)

            result.pop()
            visited[i] = False

min_ = 10 ** 11
max_ = 0
sol(0)

print(str(max_).zfill(k + 1))
print(str(min_).zfill(k + 1))