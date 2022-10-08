import sys
sys.stdin = open('4_BOJ_게임을만든동준이.txt', 'r')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.reverse()

total = 0
now = nums[0] - 1
for i in range(1, n):
    if nums[i] < now:
        now = nums[i]
    else:
        total += (nums[i] - now)
    now -= 1

print(total)