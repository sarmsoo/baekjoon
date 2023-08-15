def find():
    m2 = 1e10
    m3 = 1e10
    for i in range(6):
        for j in range(6):
            if i + j == 5:
                continue
            if i == j:
                continue
            m2 = min(m2, arr[i] + arr[j])

            for k in range(6):
                if i + k == 5 or j + k == 5:
                    continue
                if i == k or j == k:
                    continue
                m3 = min(m3, arr[i] + arr[j] + arr[k])
    return m2, m3


n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(sum(arr) - max(arr))
    exit(0)

m1 = min(arr)
m2, m3 = find()

num_of_m3 = 4
num_of_m2 = (8 * (n - 2) + 4)
num_of_m1 = 5 * n ** 2 - (3 * num_of_m3 + 2 * num_of_m2)

answer = m1 * num_of_m1 + m2 * num_of_m2 + m3 * num_of_m3
print(answer)