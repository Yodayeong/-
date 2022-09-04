## [BOJ20001 / 고무오리 디버깅]

### 문제

고무오리는 최근 풀던 문제를 해결해준다.

'고무오리 디버깅 시작'이 입력될 때부터 '고무오리 디버깅 끝'이 입력될 때까지, 문제 풀기 활동을 해라.

단, 풀 문제가 없는데 고무오리를 사용했다면, 두 문제를 더 추가해준다.



### 내가 생각해준 방법

'괄호' 문제처럼 나중에 들어온 것이 먼저 나가는 stack 구조 활용



### 내가 짠 코드

(원리)

- '문제'가 입력되면 stack에 push를 해주고
- '고무오리'가 입력되면 stack에서 pop해준다.
- 이때 '고무오리'가 입력되었는데 stack에 pop해줄 것이 없다면, stack에 두번 push를 해준다.
- 고무오리 디버깅이 끝났는데 stack에 문제가 남아있다면 '힝구' 출력
- 그게 아니라면 '고무오리야 사랑해' 출력

```python
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
```

