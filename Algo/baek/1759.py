from sys import stdin
input = stdin.readline

l, c = map(int, input().split())
alp = input().strip().split()
alp.sort()
result = []

# num_c: 자음 개수, num_v: 모음 개수
def sol(cnt, start, num_c, num_v):
    if cnt == l:
        if num_c < 2 or num_v == 0:
            return
        else:
            print(''.join(result)) # 띄어쓰기 아니다
            return

    for i in range(start, c):
        # 모음일 때
        if alp[i] in ['a', 'e', 'i', 'o', 'u']:
            result.append(alp[i])
            sol(cnt + 1, i + 1, num_c, num_v + 1)
        # 자음일 때
        else:
            result.append(alp[i])
            sol(cnt + 1, i + 1, num_c + 1, num_v)

        result.pop()

sol(0, 0, 0, 0)