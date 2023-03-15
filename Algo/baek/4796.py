i = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0:
        break
    answer = 0
    while v > 0:
        answer += min(l, v)
        v -= p
    print(f"Case {i}: {answer}")
    i += 1