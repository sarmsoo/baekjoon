from sys import stdin
import math
input = stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    lcm = math.lcm(m, n)
    flag = False
    for i in range(lcm // m):
        answer = m * i + x  
        for j in range(lcm // n):
            if answer == n * j + y:
                print(answer)
                flag = True
                break
        if flag:
            break
    if not flag:
        print(-1)