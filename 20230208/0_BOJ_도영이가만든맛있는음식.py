from itertools import combinations
import sys
sys.stdin = open('0_BOJ_도영이가만든맛있는음식.txt', 'r')

#변수들을 받아준다.
select = int(input())

foods = []
for i in range(select):
    sour, bitter = map(int, input().split())
    foods.append((sour, bitter))

#신맛과 쓴맛의 차이를 담아줄 변수
results = []

for i in range(1, select+1):

    #1개 ~ n개까지 재료들을 조합하여 combination_sets에 담아준다.
    combination_sets = list(combinations(foods, i))
    
    #combination_sets를 돌면서
    for j in combination_sets:

        #신맛과 쓴맛을 초기화 해주고
        sour = 1
        bitter = 0

        #해당 조합의 두 값들을 sour와 bitter에 곱하고 더해준다.
        for x, y in j:
            sour *= x
            bitter += y

        #results에 각 조합의 신맛과 쓴맛의 차를 넣어준다.
        results.append(abs(sour-bitter))

#results에서 가장 작은 값을 출력한다.
print(min(results))
