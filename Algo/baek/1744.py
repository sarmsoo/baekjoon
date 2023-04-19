from sys import stdin
input = stdin.readline

n = int(input())
pos = []
neg = []
zero = 0
answer = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    elif num == 0:
        zero += 1
pos.sort()
neg.sort(reverse=True)

while len(pos) > 1:
    if pos[-1] == 1:
        break
    first = pos.pop()

    if pos[-1] != 1:
        second = pos.pop()
        answer += first * second
    else:
        answer += first

if len(pos):
    if pos[-1] == 1:
        answer += len(pos)
    else:
        answer += pos[0]

while len(neg) > 1:
    first = neg.pop()
    second = neg.pop()

    answer += first * second

if len(neg):
    if zero == 0:
        answer += neg.pop()

print(answer)