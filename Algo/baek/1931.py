n = int(input())
table = []
for _ in range(n):
    start, end = map(int, input().split())
    table.append((start, end))

# 회의가 끝나는 시간이 제일 작아야함
table.sort(key=lambda x: x[0])
# 시작 시간으로도 한 번 정렬해야함
table.sort(key=lambda x: x[1])
prev_end = 0
answer = 0
for start, end in table:
    if start >= prev_end:
        answer += 1
        prev_end = end
print(answer)

'''
시작 시간으로 정렬해야하는 이유
ex) 1 3
    3 6
    3 3
이렇게 정렬 되면 3 3은 카운팅 되지않아서 결과값이 2가됨
정답은 3인데.
'''