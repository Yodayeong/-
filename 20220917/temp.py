import sys
sys.stdin = open('2_BOJ_민식어.txt', 'r')

minsik = {
    'a': 1, 'b': 2, 'k': 3, 'd': 4, 'e': 5, 'g': 6, 'h': 7, 'i': 8, 'l': 9, 'm': 10,'n': 11, 'ng': 12, 'o': 13, 
    'p': 14, 'r': 15, 's': 16, 't': 17, 'u': 18, 'w': 19, 'y': 20
    }

n = int(input())

words = []
for _ in range(n):
    temp = input()

    word = []
    for l in temp:
        word.append(minsik[l])
    
    words.append(word)

#재귀함수?
def select_smallest(word_list):
    #가장 작은 수 찾아주기
    minest = word_list[0][0]
    for i in range(1, len(word_list)):
        if word_list[i][0] < minest:
            minest = word_list[i][0]

    #가장 작은 수가 들어있는 리스트 모음
        #만약 그 모음이 하나다 => 출력
        #만약 그 모음이 여러개다 => 다음 문자열을 재귀함수로