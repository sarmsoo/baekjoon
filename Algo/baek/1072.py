from sys import stdin
input = stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
    exit(0)

left, right = 1, x
answer = 0
while left <= right:
    mid = (left + right) // 2
    nz = (y + mid) * 100 // (x + mid)
    if nz > z:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)