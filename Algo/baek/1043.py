from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
num_who_know, *people_who_know = list(map(int, input().split()))

checked = [False] * (n + 1) # 사실을 아는 사람들
for i in people_who_know:
    checked[i] = True

cnt = 0
check_list = [[] for _ in range(n + 1)] # 사람들이 참여했던 거짓을 말한 파티를 기록
party = [] # 각 파티에 참여했던 사람들을 기록
check_set = set()

def bfs(party_index):
    visited = [False] * (m + 1)
    q = deque([party_index])
    visited[party_index] = True
    while q:
        curr_party_index = q.popleft()
        check_set.add(curr_party_index)

        for i in party[curr_party_index]:
            checked[i] = True # 이거 안해줘서 계속 틀렸음
            for next_party_index in check_list[i]:
                if visited[next_party_index]:
                    continue
                q.append(next_party_index)
                visited[next_party_index] = True

for party_index in range(m):
    num_party, *curr_party = list(map(int, input().split()))
    party.append(curr_party)
    flag = False
    for people in curr_party:
        if checked[people]:
            flag = True
            break
    # 현재 파티에 사실을 아는 사람이 있는 경우
    if flag:
        for people in curr_party:
            checked[people] = True # 사실을 아는 사람이 있는 파티인 경우, 그 파티에 참석한 모든 사람이 사실을 알게됨.

            # 사실을 알게 된 사람들이 참석한 이전 파티들 중 지민이가 거짓을 말한 파티들을 check_set에 넣어줌.
            # 출력값이 cnt - len(check_set)임.
            if check_list[people]:
                for party_index in check_list[people]:
                    bfs(party_index)

    # 현재 파티에 사실을 아는 사람이 아무도 없는 경우
    else:
        cnt += 1
        # 각 사람이 참여한 거짓을 말한 파티를 기록하기 위한 코드
        for people in curr_party:
            check_list[people].append(party_index)

print(cnt - len(check_set))