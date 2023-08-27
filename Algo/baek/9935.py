from sys import stdin
input = stdin.readline

s = input().strip()
bomb = input().strip()

stack = []

for i in range(len(s)):
    stack.append(s[i])
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")