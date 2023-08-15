from sys import stdin
input = stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())

words.sort()

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if len(words[i]) > len(words[j]):
            break
        if words[i] == words[j][:len(words[i])]:
            cnt += 1
            break

print(n - cnt)