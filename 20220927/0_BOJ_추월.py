import sys
sys.stdin = open('0_BOJ_추월.txt', 'r')

n = int(sys.stdin.readline())
input = [sys.stdin.readline().rstrip() for _ in range(n)]
output = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for i in range(n):
    prior_cars = input[:i]

    now = output.index(input[i])

    for car in prior_cars:
        if car in output[now:]:
            cnt += 1
            break

print(cnt)