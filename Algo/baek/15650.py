n, m = map(int, input().split())

nums = [i + 1 for i in range(n)]
arr = [0]

def dfs(cnt):
    if cnt == m:
        print(*arr[1:])
        return

    for i in range(n):
        if arr[-1] >= nums[i]:
            continue

        arr.append(nums[i])

        dfs(cnt + 1)

        arr.pop()

dfs(0)