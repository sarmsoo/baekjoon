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
        if visited[i]:
            continue
        if nums[i] != prev and (len(arr) == 0 or arr[-1] <= nums[i]):
            prev = nums[i]
            visited[i] = True
            arr.append(nums[i])

            dfs(cnt + 1)

            visited[i] = False
            arr.pop()

dfs(0)