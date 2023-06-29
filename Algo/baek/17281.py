'''
리스트 인덱싱 최소화 하자.
for inning in range(n):
    ~
    hit = table[inning][box[curr]]
    : 시간 초과

for inning in table:
    ~
    hit = inning[box[curr]]
    : 시간 초과 x

주자들을 base = [0] * 4와 같이 list를 다루고 계산할 때는 시간 초과
하지만, base1, base2, base3 =0, 0, 0 와 같이 하니 시간 초과x
'''
from sys import stdin
input = stdin.readline

def baseball(box: list[int]) -> int:
    score = 0
    curr = -1
    for inning in table:
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out < 3:
            curr = (curr + 1) % 9
            hit = inning[box[curr]]
            if hit == 0:
                out += 1
                continue
            if hit == 1:
                score += base3
                base3, base2, base1 = base2, base1, 1
                continue
            if hit == 2:
                score += (base3 + base2)
                base3, base2, base1 = base1, 1, 0
                continue
            if hit == 3:
                score += (base3 + base2 + base1)
                base3, base2, base1 = 1, 0, 0
                continue
            if hit == 4:
                score += (base3 + base2 + base1 + 1)
                base3, base2, base1 = 0, 0, 0
                continue
    return score

def sol(depth: int) -> None:
    global answer
    if depth == 9:
        answer = max(answer, baseball(box))
        return
    if depth == 3:
        sol(depth + 1)
        return

    for i in range(1, 9):
        if visited[i]:
            continue
        box[depth] = i
        visited[i] = True

        sol(depth + 1)

        box[depth] = -1
        visited[i] = False

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * 9
box = [-1, -1, -1, 0, -1, -1, -1, -1, -1]
answer = 0

sol(0)
print(answer)