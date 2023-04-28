n = int(input())
k = int(input())

dp =[[0]] + [[0] * (i + 2) for i in range(n)] # dp[n][k], n: 총 색의 개수, k: 색을 선택하는 수
for i in range(n + 1):
    dp[i][0] = 1
    if i >= 1:
        dp[i][1] = i

for i in range(4, n + 1):
    for j in range(2, i // 2 + 1):
        if j == i / 2:
            dp[i][j] = 2
        else:
            '''
             어떠한 색을 하나를 우선 선택함(fixed)
             그럼 선택한 색의 양 옆은 뽑지 못하고 선택한 색도 뽑지 못하니
             i - 3개의 색에서 j - 1개의 색을 뽑는 경우가 됨.
             여기서 중요한 점은 위의 경우가 원에서 뽑는 경우가 아니라 
             일렬로 나열된 경우에서 뽑는 경우랑 같음.
             일렬로 나열된 경우에서 뽑는 것은 원에서 뽑는 경우를 포함하고 있음.
             그래서 우선 dp[i - 3][j - 1](원에서 뽑는 경우)을 더해줌.
             그럼 이제 원에서 뽑는 경우가 아닌 경우를 생각해보면
             일렬로 나열된 경우에서 처음과 끝에 배치한 경우임.
             이 경우가 아래 while문임.
             이렇게 다 계산한 후 맨 처음에 선택할 수 있는 색의 개수 i를 곱해주고
             중복을 제거 하기 위해 j를 나눠줌.
            '''
            # 다른 풀이가 구글에 전부이지만, 나는 이렇게 자력으로 풀었음.
            l = i - 3
            m = j - 1
            tmp = dp[l][m]
            while True:
                l -= 4
                m -= 2
                if m < 0:
                    break
                elif m == 1:
                    tmp += l
                    break
                elif m == 0:
                    tmp += 1
                    break
                else:
                    tmp += dp[l][m]
            dp[i][j] = i * tmp // j

print(dp[n][k] % 1000000003)