import sys
sys.stdin = open('0_BOJ_나이순정렬.txt', 'r')

n = int(sys.stdin.readline())
people = [tuple(sys.stdin.readline().split()) for _ in range(n)]

index = 0
#새로운 순서대로 값을 저장해줄 리스트
stack = [] 
for i in range(n):
    #미리 받아놓은 people리스트를 하나씩 순회
    temp = people[index]

    #만약 stack이 비어있다면, 그냥 값추가
    if len(stack) == 0:
        stack.append(temp)
    #만약 stack이 비어있지 않다면,
    else:
        for j in range(len(stack)):
            #나보다 큰 값이 있다면, 그 앞에 추가
            #그러나 추가 해야할 위치가 0이냐 아니냐에 따라 달라짐
            if int(temp[0]) < int(stack[j][0]):
                if j == 0:
                    stack.insert(0, temp)
                    break
                else:
                    stack.insert(j-1, temp)
                    break
            
            #stack의 길이만큼 돌았는데도 나보다 큰 값이 없다면 맨 마지막에 추가
            if j == len(stack) - 1:
                stack.append(temp)

    index += 1

#전체 stack 출력
for i in stack:
    print(*i)
