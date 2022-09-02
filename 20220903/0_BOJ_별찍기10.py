#별찍기-10

import sys
sys.stdin = open('0_BOJ_별찍기10.txt', 'r')

n = int(input())

#n=3일때부터 시작
start = 3
stars = ['***', '* *', '***']

def star(n, x):
    global start
    global stars

    #종료조건
    if n == 3:
        return

    #한번 돌때마다 패턴 초기화
    pattern = []

    #패턴을 만들어주기
    #위, 중간, 아래로 나누어서 만들어줌
    #삼차원 배열로 만들어줌
    for i in stars:
        pattern.append(i*3)

    for i in stars:
        pattern.append(i+' '*start+i)

    for i in stars:
        pattern.append(i*3)
    
    #만든 패턴을 stars에 넣어주고 start 값 증가
    stars = pattern
    start *= 3

    #종료조건
    if start == n:
        return

    star(n, start)

star(n, 0)
for i in range(n):
    print(stars[i], end='\n')