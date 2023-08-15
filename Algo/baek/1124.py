def prime_factorization(num, i):
    global num_of_primes
    if num == 1:
        return
    if is_prime(num) == 2:
        num_of_primes += 1
        return

    while True:
        if num % i == 0:
            num_of_primes += 1
            prime_factorization(num // i, i)
            break
        else:
            i += 1
    return

def is_prime(num):
    if dp[num] != 0:
        return dp[num]

    for i in range(2, int(num ** 0.5) + 1):
        # 소수 아닐 때
        if num % i == 0:
            dp[num] = 1
            return dp[num]

    dp[num] = 2
    return dp[num]


a, b = map(int, input().split())

dp = [0] * 100001
dp[1] = 1

answer = 0
for num in range(a, b + 1):
    num_of_primes = 0
    prime_factorization(num, 2)
    if is_prime(num_of_primes) == 2:
        answer += 1

print(answer)