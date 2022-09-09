import sys
sys.stdin = open('0_BOJ_균형잡힌세상.txt', 'r')

while True:
    line = sys.stdin.readline()

    if line[0] == '.':
        break

    check = 0
    stack = []
    for i in line:
        if i == '(':
            stack.append('(')
        if i == '[':
            stack.append('[')
        if i == ')':
            if len(stack) == 0:
                check = 1
                break
            temp = stack.pop()
            if temp != '(':
                check = 1
                break
        if i == ']':
            if len(stack) == 0:
                check = 1
                break
            temp = stack.pop()
            if temp != '[':
                check = 1
                break

    if len(stack) > 0:
        check = 1

    if check == 0:
        print('yes')
    else:
        print('no')