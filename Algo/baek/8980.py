from sys import stdin
input = stdin.readline

n, c = map(int, input().split())
m = int(input())
box = [list(map(int, input().split())) for _ in range(m)]
box.sort(key=lambda x: x[1])

remains = [c] * (n + 1)
answer = 0

for i in range(m):
    tmp = min(box[i][2], c)
    for j in range(box[i][0], box[i][1]):
        tmp = min(tmp, remains[j])
    for k in range(box[i][0], box[i][1]):
        remains[k] -= tmp
    answer += tmp

print(answer)