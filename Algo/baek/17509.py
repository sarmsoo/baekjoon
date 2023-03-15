D = []
V = []
for _ in range(11):
    d, v = map(int, input().split())
    D.append(d)
    V.append(v)

D.sort()
answer = 0
time = 0
for d in D:
    time += d
    answer += time
answer += 20 * sum(V)
print(answer)