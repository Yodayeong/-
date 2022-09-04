import sys
sys.stdin = open('0_BOJ_괄호.txt', 'r')

T = int(input())

for _ in range(T):
    #하나의 테스트 케이스마다 stack, check 초기화 및 기호 입력받기
    stack = []
    check = 1
    line = input()
    
    #기호가 '('이면 push, ')'이면 pop
    #1. pop을 해야하는데 stack에 아무것도 없으면 VPS가 아님
    #2. 기호를 모두 처리했는데도 stack에 무언가 남아있다면 VPS가 아님
    #VPS가 아니라면, check를 0으로 바꾸어줌
    for i in line:
        if i == '(':
            stack.append('(')
        if i == ')':
            if len(stack) == 0:
                check = 0
            else:
                stack.pop()

    if len(stack) > 0:
        check = 0

    #check가 0이면(VPS가 아니면) 'NO'를 출력
    if check == 0:
        print('NO')
    else:
        print('YES')