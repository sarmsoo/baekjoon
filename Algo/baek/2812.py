from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())
q = deque(input().strip())
stack = [q.popleft()]

while k > 0 and q:
    num = q.popleft()
    while k > 0 and stack:
        if num <= stack[-1]:
            break
        if num > stack[-1]:
            k -= 1
            stack.pop()

    stack.append(num)

# k가 아직 남았을 때
while k > 0:
    stack.pop()
    k -= 1

front = ''.join(stack)
back = ''.join(q)
print(front + back)