from sys import stdin
input = stdin.readline

n = int(input())
words = set()
for _ in range(n):
    word = input().strip()
    words.add(word)

words = list(words)
words.sort(key=lambda x: (len(x), x)) # 다중 조건 정렬

for word in words:
    print(word)