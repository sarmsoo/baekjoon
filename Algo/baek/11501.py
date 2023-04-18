from sys import stdin
input = stdin.readline
'''
for _ in range(int(input())):
    n = int(input())
    answer = 0

    stocks = list(enumerate(list(map(int, input().split()))))
    sorted_stocks = sorted(stocks, key=lambda x: x[1])

    prev = 0
    while sorted_stocks:
        index, value = sorted_stocks.pop()
        if prev < index:
            for i in range(prev, index):
                if value > stocks[i][1]:
                    answer += value - stocks[i][1]
            prev = index

    print(answer)
'''

for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    value = 0
    max = 0
    for i in range(len(stocks) - 1, -1, -1):
        if stocks[i] > max:
            max = stocks[i]
        else:
            value += max - stocks[i]

    print(value)