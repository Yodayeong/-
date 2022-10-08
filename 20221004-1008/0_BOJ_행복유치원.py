import sys
sys.stdin = open('0_BOJ_행복유치원.txt', 'r')

n, k = map(int, input().split())
heights = list(map(int, input().split()))

abstraction = []
for i in range(1, n):
    abstraction.append(heights[i] - heights[i-1])

abstraction.sort()

result = []
for i in range(n-k):
    result.append(abstraction[i])

print(sum(result))