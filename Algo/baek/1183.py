from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append(a - b)

if n % 2 != 0:
    print(1)
else:
    arr.sort()
    print(arr[n // 2] - arr[n // 2 - 1] + 1)

'''
증명은 
abs(x - a_i) 그래프 모두 그려놓고 x절편 기준으로 나눠보면 증명 아이디어 얻어짐. 
'''