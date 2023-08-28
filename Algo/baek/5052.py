from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = [input().strip() for _ in range(n)]

    nums.sort()

    flag = False
    for i in range(n - 1):
        if nums[i] == nums[i + 1][:len(nums[i])]:
            flag = True
            break
    if flag:
        print("NO")
    else:
        print("YES")