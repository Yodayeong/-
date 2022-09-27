## [BOJ10814 / 나이순 정렬]

### 문제

- 나이가 증가하는 순으로 회원 정렬
- 이때, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬



### 내가 생각해준 방법

- stack에 하나하나 쌓임

  


### 내가 짠 코드

(원리)

- stack이 비어있다면, 그냥 값 추가
- stack이 비어있지 않다면,
  - 해당 인덱스보다 큰 값이 나오기 전에 값을 추가
  - 만약, 인덱스를 모두 돌았는데도 나보다 큰 값이 없다면 맨 마지막에 추가



```python
import sys

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
```



## 문제점

시간초과가 뜸...



## lambda 표현식

: lambda 표현식으로 익명 함수 만들기



- **lambda 매개변수 : 표현식**

  - ex) def hap(x, y):

    - return x + y
- => (lambda x,y : x + y)(10, 20)



```python
import sys

#n과 people을 모두 입력받아줌
n = int(sys.stdin.readline())
people = [tuple(sys.stdin.readline().split()) for _ in range(n)]

#key값을 (int로 변환해준 people의 첫번째 인덱스)로 두고 people을 sort 해줌
people.sort(key = lambda x:int(x[0]))

#sort한 people을 출력해줌
for person in people:
    print(*person)
```
