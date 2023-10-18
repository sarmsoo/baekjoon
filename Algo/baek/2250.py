from sys import stdin
input = stdin.readline

def inorder(node):
    global order
    if node == -1:
        return
    inorder(tree[node][0])
    tree[node][4] = order
    order += 1
    inorder(tree[node][1])

def dfs(node, depth):
    global max_depth
    if node == -1:
        return
    tree[node][3] = depth
    max_depth = max(max_depth, depth)
    dfs(tree[node][0], depth + 1)
    dfs(tree[node][1], depth + 1)


n = int(input())
# [left, right, parent, depth, width]
tree = [[0] * 5 for _ in range(n + 1)]
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node][0] = left
    tree[node][1] = right

    if left != -1:
        tree[left][2] = node
    if right != -1:
        tree[right][2] = node

root = 0
for i in range(1, n + 1):
    if tree[i][2] == 0:
        root = i

order = 1
inorder(root)

max_depth = 1
dfs(root, 1)

tmp = [[n, 0] for _ in range(max_depth + 1)]
for i in range(1, n + 1):
    tmp[tree[i][3]][0] = min(tmp[tree[i][3]][0], tree[i][4])
    tmp[tree[i][3]][1] = max(tmp[tree[i][3]][1], tree[i][4])

tmp = [tmp[i][1] - tmp[i][0] + 1 for i in range(max_depth + 1)]

min_level = n
max_width = 0
for i in range(1, max_depth + 1):
    if max_width < tmp[i]:
        max_width = tmp[i]
        min_level = i

print(min_level, max_width)