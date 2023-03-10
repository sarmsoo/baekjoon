from sys import stdin
input = stdin.readline

m = int(input())

s = set()
for _ in range(m):
    string = input().split()
    if len(string) == 2:
        calc, x = string[0], int(string[1])
    else:
        calc = string[0]

    if calc == 'add':
        s.add(x)
    elif calc == 'remove':
        s.discard(x)
    elif calc == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif calc == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif calc == 'all':
        s = set(range(1, 21))
    elif calc == 'empty':
        s.clear()