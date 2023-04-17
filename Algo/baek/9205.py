from sys import stdin
from collections import deque
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    home_x, home_y = map(int, input().split())
    stores = []
    for _ in range(n):
        stores.append(list(map(int, input().split())))
    r_x, r_y = map(int, input().split())

    q = deque([[home_x, home_y]])
    visited = [[home_x, home_y]]
    flag = True
    while q:
        c_x, c_y = q.popleft()

        if abs(c_x - r_x) + abs(c_y - r_y) <= 1000:
            print("happy")
            flag = False
            break

        for store in stores:
            store_x, store_y = store
            if abs(c_x - store_x) + abs(c_y - store_y) <= 1000:
                visited.append(store)
                q.append(store)
                stores.remove(store)

    if flag:
        print("sad")