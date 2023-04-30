from sys import stdin
input = stdin.readline

n = int(input())
seq = [0] + [int(input()) for _ in range(n)]
stack = []

flag = False
prev = 0
buffer = []

for i in range(1, n + 1):
    if seq[i] > seq[i - 1]:
        for j in range(prev + 1, seq[i] + 1):
            stack.append(j)
            buffer.append('+')
        buffer.append('-')
        stack.pop()
        prev = seq[i]

    elif seq[i] < seq[i - 1]:
        if stack[-1] == seq[i]:
            buffer.append('-')
            stack.pop()
        else:
            flag = True
            break

if flag:
    print("NO")
else:
    for i in buffer:
        print(i)