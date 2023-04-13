n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        arr.append(nums[i])

        dfs(cnt + 1)

        arr.pop()

dfs(0)