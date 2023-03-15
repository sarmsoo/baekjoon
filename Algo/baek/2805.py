n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 1
end = max(heights)

while start <= end:
    mid = (start + end) // 2
    hap = 0
    for height in heights:
        if height > mid:
            hap += height - mid

    if hap >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

"""
왜 이 문제 16564 방식으로 풀면 왜 안되냐 진짜...?
한 번 재대로 분석해보자 그리고 12738 풀어서 맞추자...
"""
