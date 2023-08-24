from sys import stdin
input = stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort()

if crane[0] < box[-1]:
    print(-1)
    exit(0)

crane = [c for c in crane if c >= box[0]] # 이 줄 없으면: 4808ms, 있으면: 128ms 엄청 차이나네

time = 0
while True:
    time += 1
    for i in range(len(crane)):
        for j in range(len(box) - 1, -1, -1):
            if crane[i] >= box[j]:
                box.pop(j)
                break

        if not box:
            print(time)
            exit(0)