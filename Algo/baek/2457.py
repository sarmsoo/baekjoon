from sys import stdin
input = stdin.readline

n = int(input())
table = []
for _ in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    table.append(((start_month, start_day), (end_month, end_day)))

table.sort()

prev_start, prev_end = (1, 1), (3, 1)
answer = 0
i = 0
tmp = (0, 0)

while True:
    if i == n:
        if tmp > prev_end and prev_end < (12, 1):
            prev_end = tmp
            answer += 1
        break

    curr_start, curr_end = table[i]

    if curr_start <= prev_end < curr_end:
        tmp = max(tmp, curr_end)
        i += 1
    elif curr_end <= prev_end:
        i += 1
    elif curr_start > prev_end:
        if prev_end != tmp:
            prev_end = tmp
            answer += 1
        else:
            break

if prev_end >= (12, 1):
    print(answer)
else:
    print(0)