from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
order = [0] + list(map(int, input().split()))
cnt = n
multi = set()
answer = 0

for i in range(1, k + 1):
    if order[i] not in multi:
        if cnt > 0:
            cnt -= 1
            multi.add(order[i])

        elif cnt == 0:
            priority = 0
            plug = 0
            flag = True
            for j in multi:
                if j not in order[i + 1:k + 1]:
                    multi.remove(j)
                    flag = False
                    break
                else:
                    for l in range(i + 1, k + 1):
                        if order[l] == j:
                            if priority < l:
                                priority = l
                                plug = j
                                break
                            elif priority > l:
                                break
            if flag:
                multi.remove(plug)

            answer += 1
            multi.add(order[i])

print(answer)