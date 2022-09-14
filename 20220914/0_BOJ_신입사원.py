import sys
sys.stdin = open('0_BOJ_신입사원.txt', 'r')

T = int(sys.stdin.readline())

for _ in range(T):

    n = int(sys.stdin.readline())
    people = [0] * (n+1)

    for i in range(n):
        score1, score2 = map(int, sys.stdin.readline().split())
        people[score1] = score2

    cnt = 0
    temp = people[1]
    for i in range(1, n+1):
        if people[i] <= temp:
            temp = people[i]
        else:
            cnt += 1
    
    print(n - cnt)