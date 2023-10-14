from sys import stdin
input = stdin.readline

def preorder(root):
    if root == '.':
        return
    result_of_pre.append(root)
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.':
        return
    inorder(tree[root][0])
    result_of_in.append(root)
    inorder(tree[root][1])

def postorder(root):
    if root == '.':
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    result_of_post.append(root)


n = int(input())
tree = dict()
for _ in range(n):
    curr, left, right = map(str, input().split())
    tree[curr] = (left, right)

result_of_pre = []
result_of_in = []
result_of_post = []

preorder('A')
inorder('A')
postorder('A')

print(''.join(result_of_pre))
print(''.join(result_of_in))
print(''.join(result_of_post))