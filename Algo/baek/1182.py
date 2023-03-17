n, s = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
current_sum = 0


def dfs(current):
    global cnt, current_sum

    if current == n:
        return
    # 현재까지의 합이 s이면 결과 +1
    if current_sum + seq[current] == s:
        cnt += 1

    # 이번 원소를 포함시키지 않고 시도
    dfs(current + 1)

    # 이번 원소를 포함하고 시도
    current_sum += seq[current]
    dfs(current + 1)

    # 마지막에 다시 이번 원소 빼주기
    current_sum -= seq[current]


dfs(0)
print(cnt)