from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    s = input().strip()
    answer = "YES"
    while len(s) > 0:
        if s.startswith("100"):
            s = s[3:]

            while len(s) > 0 and s.startswith('0'):
                s = s[1:]

            if len(s) == 0:
                answer = "NO"
                break

            s = s[1:]

            while len(s) > 0 and s.startswith('1'):
                if len(s) >= 3 and s[1] == '0' and s[2] == '0':
                    break
                else:
                    s = s[1:]
        elif s.startswith("01"):
            s = s[2:]
        else:
            answer = "NO"
            break

    print(answer)