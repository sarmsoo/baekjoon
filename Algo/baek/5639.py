from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    post(start + 1, mid - 1)
    post(mid, end)
    print(pre[start])


pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

post(0, len(pre) - 1)