n = int(input())

if n == 1:
    print(0)
    exit(0)

is_prime = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False

answer = 0
if primes[-1] == n:
    answer += 1

left, right = len(primes) - 3, len(primes) - 2
while left >= 0:
    if left == right:
        left -= 1
    sum_ = sum(primes[left:right + 1])
    if sum_ == n:
        answer += 1
        right -= 1
    elif sum_ > n:
        right -= 1
    elif sum_ < n:
        left -= 1

print(answer)