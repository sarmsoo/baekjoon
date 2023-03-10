n = int(input())

two, five = 0, 0
for i in range(1, n+1):
    while True:
        if i % 5 == 0:
            five += 1
            i = i / 5
        elif i % 2 == 0:
            two += 1
            i = i / 2
        else:
            break
print(min(two, five))