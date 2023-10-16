from sys import stdin
input = stdin.readline

def dfs(num):
    tree[num] = -2
    for i in range(n):
        if num == tree[i]:
            dfs(i)


n = int(input())
tree = list(map(int, input().split()))
k = int(input())

dfs(k)
answer = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        answer += 1

print(answer)