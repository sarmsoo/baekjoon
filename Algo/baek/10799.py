from sys import stdin
input = stdin.readline

s = input().strip()

answer = 0
c = 0
i = 0
while i < len(s):
    if s[i] == '(':
        if s[i + 1] == ')':
            answer += c
            i += 2
        else:
            c += 1
            i += 1
    else:
        answer += 1
        c -= 1
        i += 1

print(answer)