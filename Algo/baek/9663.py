n = int(input())
graph = [[0] * n for _ in range(n)]

dy = [1, 1, 1]
dx = [0, 1, -1]
def checking(y, x, flag):
    if flag:
        graph[y][x] += 1
    else:
        graph[y][x] -= 1
    for i in range(3):
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                break
            if flag:
                graph[ny][nx] += 1
            else:
                graph[ny][nx] -= 1

def sol(start_y, cnt):
    global result
    if cnt == n:
        result += 1
        return

    for x in range(n):
        if graph[start_y][x]:
            continue
        checking(start_y, x, True)

        sol(start_y + 1, cnt + 1)

        checking(start_y, x, False)

result = 0
sol(-1, 0)
print(result)
# 응~ 혼자 풀었었어~

# 다른 사람 풀이, 훨씬 깔끔하다.
'''
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
'''