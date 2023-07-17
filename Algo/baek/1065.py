from sys import stdin
input = stdin.readline

n = int(input())

answer = 0
for i in range(1, n + 1):
    answer += 1
    if i < 100:
        continue

    prev = int(str(i)[0]) - int(str(i)[1])
    for j in range(2, len(str(i))):
        tmp = int(str(i)[j - 1]) - int(str(i)[j])
        if not tmp == prev:
            answer -= 1
            break
        prev = tmp

print(answer)