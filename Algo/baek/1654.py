"""랜선 자르기"""

n, k = map(int, input().split())
lan = [int(input()) for _ in range(n)]
start = 1
end = (sum(lan) // n) + 1

while start <= end:
    mid = (start + end) // 2
    hap = 0
    for i in range(n):
        hap += lan[i] // mid

    if hap >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)

"""이분 탐색"""
# end 설정을 min(lan)으로 해버리면 안됨 만약 k = 1이면 바로 최대 래선은 max(lan)임



