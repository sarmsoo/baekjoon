n = int(input())
peoples = list(map(int, input().split()))
peoples.sort()

answer = []
temp = 0
for people in peoples:
    temp += people
    answer.append(temp)
print(sum(answer))