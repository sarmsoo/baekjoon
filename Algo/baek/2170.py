from sys import stdin
input = stdin.readline
'''
n = int(input())
result = []
lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort()

for i in range(n):
    curr_start, curr_end = lines[i]

    j = 0
    flag = True
    while result and j < len(result):
        start, end = result[j]
        if start <= curr_start <= end:
            result[j] = (start, max(end, curr_end))
            flag = False
            break

        elif curr_start < start:
            if curr_end >= start:
                result[j] = (curr_start, max(curr_end, end))
                flag = False
                break
        j += 1

    if flag:
        result.append((curr_start, curr_end))

answer = 0
for line in result:
    start, end = line
    answer += end - start

print(answer)
'''

n = int(input())
lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))
lines.sort()
answer = 0
start, end = lines[0][0], lines[0][1]

for i in range(1, n):
    if lines[i][0] <= end < lines[i][1]:
        end = max(end, lines[i][1])

    elif lines[i][0] > end:
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]

answer += end - start
print(answer)