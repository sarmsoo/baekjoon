from sys import stdin
input = stdin.readline

def change(a, b):
    a_copy = a[:]
    cnt = 0
    for i in range(1, n):
        if a_copy[i - 1] == b[i - 1]:
            continue

        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                a_copy[j] = 1 - a_copy[j]

    if a_copy == b:
        return cnt
    return 1e10

n = int(input())
init = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

answer = change(init, goal)

init[0] = 1 - init[0]
init[1] = 1 - init[1]
answer = min(answer, change(init, goal) + 1)

print(answer if answer != 1e10 else -1)