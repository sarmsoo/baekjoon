n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input().strip())
    coins.append(coin)
answer = 0
for coin in coins[::-1]:
    if k >= coin:
        answer += k // coin
        k = k % coin
print(answer)