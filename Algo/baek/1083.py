from sys import stdin
input = stdin.readline

def find_max_idx(start, length):
    result = 0
    max_ = 0
    for i in range(start, min(len(arr), start + length + 1)):
        if arr[i] > max_:
            result = i
            max_ = arr[i]
    return result

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

sorted_arr = sorted(arr, reverse=True)

i = 0
while i < n and s > 0:
    max_idx = find_max_idx(i, s)
    for j in range(max_idx, i, -1):
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
    s -= max_idx - i
    i += 1
    if arr == sorted_arr:
        break

print(*arr)