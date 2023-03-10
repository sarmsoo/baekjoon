from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())

for _ in range(t):
    clacs = input().strip()
    n = int(input())
    if n == 0:
        l = deque(input())
        l = deque()
    else:
        l = deque(input().strip()[1:-1].split(","))


    flag = True
    rev = 0
    for clac in clacs:
        if clac == "R":
            rev += 1

        elif clac == "D":
            if l:
                if rev % 2 == 0:
                    l.popleft()
                else:
                    l.pop()
            else:
                print("error")
                flag = False
                break

    if flag:
        if rev % 2 != 0:
            l.reverse()
        print("["+",".join(l)+"]")