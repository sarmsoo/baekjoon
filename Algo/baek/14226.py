from collections import deque

s = int(input())
q = deque()
q.append((1, 0))
visited = [[False] * 1001 for _ in range(1001)]

time = 0
while q:
    for _ in range(len(q)):
        curr, clip = q.popleft()
        if curr == s:
            print(time)
            exit(0)
        for i in range(3):
            if i == 0:
                new_curr, new_clip = curr + clip, clip
            elif i == 1:
                new_curr, new_clip = curr, curr
            elif i == 2:
                new_curr, new_clip = curr - 1, clip

            if new_curr > 1000 or new_curr < 0 or new_clip > 1000 or new_clip < 0:
                continue
            if visited[new_curr][new_clip]:
                continue
            visited[new_curr][new_clip] = True
            q.append((new_curr, new_clip))
    time += 1