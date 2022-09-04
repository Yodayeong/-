import sys
sys.stdin = open('2_BOJ_고무오리디버깅.txt', 'r', encoding='UTF-8')

#빈 스택 준비
stack = []

#무한반복문을 돌리는데
while True:
    get_input = input()

    #'고무오리 디버깅 끝'이 입력되면 break
    if get_input == '고무오리 디버깅 끝':
        break
    #'문제'가 입력되면 stack에 push
    if get_input == '문제':
        stack.append('문제')
    #'고무오리'가 입력되면
    if get_input == '고무오리':
        #stack에 아무것도 없으면 stack에 push 두번
        if len(stack) == 0:
            stack.append('문제')
            stack.append('문제')
        #그게 아니랴면 가장 최근의 문제 pop
        else:
            stack.pop()

#stack에 문제가 남아있다면 '힝구' 출력
if len(stack) > 0:
    print('힝구')
#그게 아니라면 '고무오리야 사랑해' 출력
else:
    print('고무오리야 사랑해')