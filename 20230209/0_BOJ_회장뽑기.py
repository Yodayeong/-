import sys
sys.stdin = open('0_BOJ_회장뽑기.txt', 'r')

#초기값들 설정 (무한, 최소비용을 저장해줄 이중배열)
INF = 100
num = int(input())
people = [[INF]*num for _ in range(num)]

#자기자신은 0으로 초기화
for i in range(num):
    people[i][i] = 0

#이중배열 채우기
while(True):
    x, y = map(int, input().split())

    if x==-1 and y==-1:
        break

    people[x-1][y-1] = 1
    people[y-1][x-1] = 1

#각 정점을 기준으로 비교
for k in range(num):
    for i in range(num):
        for j in range(num):
            #작을수록 좋기 때문에 값이 더 작다면 값을 갱신
            if people[i][k] + people[k][j] < people[i][j]:
                people[i][j] = people[i][k] + people[k][j]

#가장 큰 값이 해당 사람이 가장 멀리까지 연결된 친구 이므로, 
#가장 큰 값을 뽑아줌
final = []
for i in range(num):
    final.append(max(people[i]))

#회장 후보의 점수
min_value = min(final)

#회장 후보
presidents = []
for i in range(num):
    if final[i] == min_value:
        presidents.append(i+1)

#정답 출력
print(min_value, len(presidents))
print(*presidents)