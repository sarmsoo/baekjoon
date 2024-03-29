'''
재미있는 문제
모든 수의 약수인 1이 중요
1을 제외한 n - 1개의 수로 게임을 했을 때 A가 이겼다면,
1을 포함하는 n개의 수로 게임을 하는 경우에도 1이 아닌 수 최적의 수를 처음에 뽑으면
1은 어차피 사라자니깐 결과는 n - 1개로 했을 떄와 같이 A가 승.

n - 1개의 수로 게임을 했을 때 A가 졌다면,
1을 포함하는 n개의 수로 하는 게임에서는 처음에 1을 뽑아버리면 A가 승.

즉, n = 1이 아닌 모든 경우 A가 이김.
'''
from sys import stdin
input = stdin.readline

n = int(input())

print('A' if n > 1 else 'B')