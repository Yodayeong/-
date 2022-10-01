import sys
sys.stdin = open('2_BOJ_무한수열.txt', 'r')

n, p, q = map(int, input().split())

values = [1, ]
for i in range(1, n+1):
    first = int(i/p)
    second = int(i/q)

    values.append(values[first] + values[second])

print(values[n])