# n = int(input())
# coors = list(map(int, input().split()))
# coors = list(enumerate(coors))
# coors.sort(key=lambda x: x[1])
#
# temp = 0
# coors[0] = coors[0] + (0,)
# for i in range(1, n):
#     if coors[i][1] != coors[i - 1][1]:
#         temp += 1
#         coors[i] = coors[i] + (temp,)
#
#     else:
#         coors[i] = coors[i] + (temp,)
#
# coors.sort(key=lambda x: x[0])
#
# for i in range(n):
#     print(coors[i][2], end=' ')

from sys import stdin
input = stdin.readline

n = int(input())
coors = list(map(int, input().split()))

new_coors = list(set(coors))
new_coors.sort()

table = {}
for i, coor in enumerate(new_coors):
    table[coor] = i

for coor in coors:
    print(table[coor], end=' ')