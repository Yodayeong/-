import sys
sys.stdin = open('0_BOJ_회장뽑기.txt', 'r')

INF = 100
num = int(input())

matrix = [[INF]*num for _ in range(num)]

for i in range(num):
    matrix[i][i] = 0

while True:
    x, y = map(int, input().split())

    if x==-1 and y==-1:
        break

    matrix[x-1][y-1] = 1
    matrix[y-1][x-1] = 1

for k in range(num):
    for i in range(num):
        for j in range(num):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

final = []
for i in range(num):
    final.append(max(matrix[i]))

print(final)