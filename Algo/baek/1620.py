from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

names = {}
nums = {}

for i in range(1, n + 1):
    name = input().strip()
    names[name] = i
    nums[i] = name

for _ in range(m):
    inp = input().strip()
    if inp.isdigit():
        print(nums[int(inp)])
    else:
        print(names[inp])