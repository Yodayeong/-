## [BOJ4949/ 균형잡힌 세상]

### 문제

- 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단
- 괄호 : '()' or '[]'
- 입력 종료조건 : 점(.) 하나
- 각 줄은 점(.)으로 끝남
- 균형을 이루면 : 'yes' / 그렇지 않으면 : 'no'



### 내가 생각해준 방법

stack에 괄호를 넣고 빼자!



### 내가 짠 코드

(원리)

괄호들의 균형이 안 맞춰져 있는 경우를 생각하자.

1. stack에서 pop 할 때 stack이 비어있는 경우
2. stack에서 pop 했는데 다른 괄호가 나온 경우
3. 종료를 했는데 stack에 괄효가 남아있는 경우



```python
import sys

while True:
    line = sys.stdin.readline()

    #점만 하나 들어온 경우에 무한 반복문 종료
    if line[0] == '.':
        break

    #check변수로 균형이 맞춰져 있는지 아닌지 체크
    check = 0
    stack = []
    for i in line:
        #왼쪽 괄호는 stack에 append
        if i == '(':
            stack.append('(')
        if i == '[':
            stack.append('[')
        #오른쪽 괄호는
        if i == ')':
            #pop하려는데 stack이 비어있으면, check 및 break
            if len(stack) == 0:
                check = 1
                break
            #stack이 비어있지는 않은데
            temp = stack.pop()
            #pop한 괄호가 다른 괄호면, check 및 break
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

    #종료했는데 stack에 괄호가 남아있는 경우도 check
    if len(stack) > 0:
        check = 1

    #check가 바뀌지 않았다면 'yes' 출력
    if check == 0:
        print('yes')
    #check가 바꼈다면 'no' 출력
    else:
        print('no')
```

