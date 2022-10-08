import sys
sys.stdin = open('2_BOJ_등수매기기.txt', 'r')

input = sys.stdin.readline

n = int(input())
ranks = [int(input()) for _ in range(n)]

ranks.sort()

total = 0
for i in range(1, n+1):
    total += abs((i - ranks[i-1]))

print(total)