from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

n = int(input())
mid = int(input())
print(mid)

upper = [] # mid 보다 큰 값
lower = [] # mid 보다 작은 값
# True: 이전 까지의 총 수의 개수가 홀수, False: 짝수
flag = True
for _ in range(1, n):
    num = int(input())
    if num == mid:
        if flag:
            heappush(upper, num)
        else:
            heappush(lower, (-num, num))
        print(mid)

    elif num < mid:
        if flag:
            heappush(lower, (-num, num))
            heappush(upper, mid)
            mid = heappop(lower)[1]
            print(mid)
        else:
            heappush(lower, (-num, num))
            print(mid)

    elif num > mid:
        if flag:
            heappush(upper, num)
            print(mid)
        else:
            heappush(upper, num)
            heappush(lower, (-mid, mid))
            mid = heappop(upper)
            print(mid)

    flag = not flag

# 같은 방식인데 이게 더 깔끔함
'''
left, right = [], []

for i in range(int(input())):
    num = int(input())

    if len(left) == len(right):
        heappush(left, -num)
    else:
        heappush(right, num)
    
    if right and -left[0] > right[0]:
        heappush(right, -heappop(left))
        heappush(left, -heappop(right))
    print(-left[0])
'''