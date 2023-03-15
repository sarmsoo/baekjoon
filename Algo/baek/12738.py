n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n
mid = 0
a = nums[0]
while start <= end:
    mid = (end + start) // 2
    m = 1
    for i in range(1, n):
        if nums[i] > a:
            m += 1
            a = nums[i]
    if m <= mid:
        end = mid - 1
    else:
        start = mid + 1

print(mid)