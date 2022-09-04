import sys
sys.stdin = open('1_BOJ_저항.txt', 'r')

#colors의 값과 곱을 dictionary로 정리
colors = {
    'black': [0, 1],
    'brown': [1, 10],
    'red': [2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue': [6, 1000000],
    'violet': [7, 10000000],
    'grey': [8, 100000000],
    'white': [9, 1000000000]
}

#3가지 색 입력받기
first = input()
second = input()
third = input()

#첫번째 색과 두번째 색은 각 키값의 첫번째 값을,
#세번째 색은 키값의 두번째 값을 가져온다.
print(((colors[first][0]*10) + colors[second][0])*colors[third][1])