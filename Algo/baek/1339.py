from sys import stdin
input = stdin.readline

n = int(input())
words = []
weight = [[0, chr(i + 65), 0] for i in range(26)]
for _ in range(n):
    word = input().strip()
    words.append(word)
    for i in range(len(word)):
        weight[ord(word[i]) - 65][0] += 10 ** (len(word) - 1 - i)

weight.sort(reverse=True)

for i in range(9):
    weight[i][2] = 9 - i

weight.sort(key=lambda x: x[1])

nums = []
for word in words:
    num = 0
    for i in range(len(word)):
        num += weight[ord(word[i]) - 65][2] * (10 ** (len(word) - 1 - i))
    nums.append(num)

print(sum(nums))