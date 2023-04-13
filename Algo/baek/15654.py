n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False] * n
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i]:
            continue

        arr.append(nums[i])
        visited[i] = True

        dfs(cnt + 1)

        arr.pop()
        visited[i] = False

dfs(0)
