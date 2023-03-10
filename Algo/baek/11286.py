from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

n = int(input())

heap = []
for _ in range(n):
    num = int(input())

    if num != 0:
        heappush(heap, (abs(num), num))

    else:
        if heap:
            temp = []
            pop = heappop(heap)

            if pop[1] < 0:
                print(pop[1])

            else:
                while heap:
                    if heap[0][0] != pop[0]:
                        break

                    n_pop = heappop(heap)

                    if n_pop[1] == pop[1]:
                        temp.append(pop)
                        pop = n_pop
                    elif n_pop[1] < pop[1]:
                        pop = n_pop
                        break
                for i in temp:
                    heappush(heap, i)
                print(pop[1])
        # heap에 아무것도 없을 때
        else:
            print(0)

'''
python tuple의 order는 각 성분이 다를 때 까지 비교하는데, 모두 같으면 같은 것
그래서 위 처럼 난리 칠 필요가 없다
'''

heap = []
for _ in range(n):
    num = int(input())

    if num != 0:
        heappush(heap, (abs(num), num))

    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)