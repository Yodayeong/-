import sys
sys.stdin = open('3_BOJ_배부른마라토너.txt', 'r')

n = int(input())

#참가자들과 그 수를 입력받기
maratoners = dict()
for i in range(n):
    maratoner = input()

    if maratoner in maratoners:
        maratoners[maratoner] += 1
    else:
        maratoners[maratoner] = 1

#완주자들은 수를 -1해주기
for i in range(n-1):
    completed = input()

    if maratoner in maratoners:
        maratoners[completed] -= 1

#결국 dictionary에서 수가 1인 참가자만 출력
for i in maratoners:
    if maratoners[i] == 1:
        print(i)