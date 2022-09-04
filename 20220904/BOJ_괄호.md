## 스택, 큐



### 스택

- 나중에 넣은 데이터가 먼저 반환되는 구조

- 리스트 활용

  - 삽입(push) => append()

  - 삭제(pop) => pop()

    

### 큐

- 먼저 넣은 데이터가 먼저 반환되는 구조
- 리스트 활용
  - 삽입(push) => append()
  - 삭제(pop) => pop(0)



## [BOJ9012 / 괄호]

### 문제

괄호 문자열은 '(', ')' 로 구성된 문자열.

그 중 괄호의 모양이 바르게 구성된 문자열을 VPS라 함.

문자열이 주어졌을때 VPS면 YES, VPS가 아니면 NO를 출력.



### 내가 생각해준 방법

나중에 들어온 것이 먼저 나가는 stack 구조를 활용해 괄호의 짝을 맞추어 준다.



### 내가 짠 코드

(원리)

- '(' 기호가 입력으로 들어오면 stack에 push 해주고, ')' 기호가 입력으로 들어오면 stack에서 pop 해준다.
- 두가지 경우에서 VPS가 아닌 것을 확인 할 수 있다.
- 1. 모든 입력을 처리했음에도 stack에 '(' 기호가 남은 경우
  2. ')' 기호를 입력받아서 stack에서 pop 해야하는데, stack에 아무것도 남아있지 않은 경우

```python
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
```