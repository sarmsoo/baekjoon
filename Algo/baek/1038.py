from collections import deque

n = int(input())

def sol(depth):
    global cnt
    if len(arr) - 1 == depth:
        cnt += 1
        if cnt == n:
            s = ""
            for j in range(1, len(arr)):
                s += str(arr[j])
            print(s)
            exit(0)
        return

    for i in range(10):
        if arr[-1] <= i:
            continue
        arr.append(i)

        sol(depth)

        arr.pop()


arr = [1e12]
cnt = -1

for d in range(1, 11):
    sol(d)
print(-1)