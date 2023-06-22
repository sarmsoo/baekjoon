'''
약간 그리디가 첨가된 백트래킹, 가장 먼저 완성된 숫자가 제일 작은 수
check도 맨 뒤에서만 해주면됨.
'''
def check(num):
    l = len(num)
    for i in range(1, l//2 + 1):
        if num[-i:] == num[-(i * 2):-i]:
            return False
    return True

def sol(depth):
    global answer
    if depth == n:
        print(''.join(list(map(str, arr))))
        exit(0)

    for i in range(1, 4):
        if len(arr) == 0 or (arr[-1] != i and check(arr + [i])):
            arr.append(i)

            sol(depth + 1)

            arr.pop()

n = int(input())
arr = []
answer = 10 ** 81
sol(0)
print(answer)