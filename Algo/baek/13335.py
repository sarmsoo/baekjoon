from sys import stdin
from collections import deque
input = stdin.readline

n, w, l = map(int, input().split())
tmp = list(map(int, input().split()))
q = deque()
for i in range(1, n + 1):
    q.append([w + i, tmp[i - 1]])

answer = 0
while q:
    answer += 1
    if q[0][0] == 1:
        q.popleft()
        if not q:
            break

    q[0][0] -= 1
    weight = q[0][1]
    cnt = 0
    for i in range(1, len(q)):
        if weight + q[i][1] <= l:
            weight += q[i][1]
            q[i][0] -= 1
        else:
            cnt = i
            break

    if q[cnt][0] <= w + 1:
        continue
    for i in range(cnt, len(q)):
        q[i][0] = q[i - 1][0] + 1

print(answer)

# 말도 안되게 어거지로 풀었다.
# 집중이 안되니깐 너무 흘러가는 대로 막 푼다.

# 다른 사람의 코드
n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)
print(time)
