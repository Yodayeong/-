import sys
sys.stdin = open('0_BOJ_랜선자르기.txt', 'r')

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

low = 1
high = max(lines)
while (low <= high):
    mid = (low + high) // 2
    line_total = 0

    for line in lines:
        line_total += line // mid

    if line_total >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)