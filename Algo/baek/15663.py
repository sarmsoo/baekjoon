n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False] * n
arr = []

def dfs(cnt):
    prev = 0
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i] or nums[i] == prev:
            continue

        prev = nums[i]
        arr.append(nums[i])
        visited[i] = True

        dfs(cnt + 1)

        arr.pop()
        visited[i] = False

dfs(0)