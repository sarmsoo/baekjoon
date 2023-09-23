from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print("A")
    exit(0)

if n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
    exit(0)

# n >= 2, 처음 두개가 같을 때
if arr[0] == arr[1]:
    flag = True
    for i in range(2, n):
        if arr[i] != arr[0]:
            flag = False
            break
    # 모두 같은 숫자일 때
    if flag:
        print(arr[0])
    # 다른 숫자가 있을 때
    else:
        print("B")
    exit(0)

a = 0
b = 0
for i in range(n - 2):
    if arr[i + 1] == arr[i]:
        continue
    else:
        a = (arr[i + 2] - arr[i + 1]) // (arr[i + 1] - arr[i])
        b = arr[i + 1] - a * arr[i]

# 구한 a, b가 맞으면 flag = True
flag = True
for i in range(n - 1):
    if arr[i + 1] != arr[i] * a + b:
        flag = False
        break

if flag:
    print(arr[n - 1] * a + b)
else:
    print("B")