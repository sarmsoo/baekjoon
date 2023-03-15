from sys import stdin
input = stdin.readline

n = int(input())
lectures = []
for _ in range(n):
    s, t = map(int, input().split())
    lectures.append((s, t))
lectures.sort(key=lambda x: x[1])
lectures.sort(key=lambda x: x[0])

c_t = 0
answer = 0
while lectures:
    c_t = 0
    i = 0
    answer += 1
    for _ in range(len(lectures)):
        n_s, n_t = lectures[i]
        if n_s >= c_t:
            c_t = n_t
            lectures.pop(i)
        else:
            i += 1
print(answer)
