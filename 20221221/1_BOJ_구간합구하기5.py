import sys

sys.stdin = open('1_BOJ_구간합구하기5.txt', 'r')

N, M = map(int, input().split())
array_N = [input().split() for _ in range(N)]
array_M = [input().split() for _ in range(M)]

for i in range(M):
    sum = 0

    for j in range(int(array_M[i][1])-1, int(array_M[i][3])):
        for k in range(int(array_M[i][0])-1, int(array_M[i][2])):
            sum += int(array_N[j][k])

    print(sum)