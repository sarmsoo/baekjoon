from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

def operation(a, b, operator):
    if operator == 0:
        return a + b
    if operator == 1:
        return a - b
    if operator == 2:
        return a * b
    if operator == 3:
        if a > 0:
            return a // b
        else:
            return -(-a // b)

def sol(result, cnt, start):
    global min_, max_
    if cnt == n - 1:
        min_ = min(min_, result)
        max_ = max(max_, result)
        return

    for i in range(4):
        if op[i] == 0:
            continue
        op[i] -= 1
        tmp = result
        result = operation(result, arr[cnt + 1], i)

        sol(result, cnt + 1, start + 1)

        op[i] += 1
        result = tmp

min_ = 1000000001
max_ = -1000000001
sol(arr[0], 0, 1)
print(max_)
print(min_)