from sys import stdin
input = stdin.readline

s = list(input().strip())
t = list(input().strip())

flag = True
while t:
    if s == t:
        print(1)
        flag = False
        break

    if t[-1] == 'A':
        t.pop()

    else:
        t.pop()
        t.reverse()

if flag:
    print(0)