arr = list(map(int, input().split()))
arr.sort(reverse=True)
arr.pop()
print(sum(arr))