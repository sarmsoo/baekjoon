from sys import stdin
input = stdin.readline

def sol(depth, start):
    global answer
    if depth == k - 5:
        tmp = 0
        for word in arr:
            tmp += 1
            for w in word:
                if w in alp:
                    continue
                tmp -= 1
                break
        answer = max(answer, tmp)
        return

    for i in range(start, 26):
        if chr(i + 97) in ['a', 'n', 't', 'i', 'c']:
            continue
        alp.append(chr(i + 97))

        sol(depth + 1, i + 1)

        alp.pop()


n, k = map(int, input().split())

if k == 26:
    print(n)
    exit(0)
if k < 5:
    print(0)
    exit(0)

arr = []
for _ in range(n):
    tmp = []
    word = input().strip()
    for i in range(len(word)):
        if word[i] in ['a', 'n', 't', 'i', 'c']:
            continue
        if word[i] in tmp:
            continue
        tmp.append(word[i])
    arr.append(tmp)

alp = []
answer = 0
sol(0, 0)

print(answer)