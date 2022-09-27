## [BOJ1946 / 신입 사원]

### 문제

- 1차 시험과 2차 시험 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자를 선발
- 즉, A가 B의 시험 성적에 비해 1차와 2차가 모두 더 낮다면, 선발하지 않음
- 성적이 순위로 주어질 때, 선발할 수 있는 최대 인원수 구하기



### 내가 생각해준 방법

- 전체 인원에서 선발될 수 없는 인원(1,2차 순위가 모두 다른 사람보다 낮은 인원) 을 빼준다.



### 내가 짠 코드

(원리)

- for문을 돌려서 각 사람들을 다른 사람들의 1, 2차 순위와 비교한다.
- 선발될 수 없는 사람의 수를 cnt 변수에 담아준다.
- 전체 인원 n에서 선발될 수 없는 인원 cnt를 빼서 최종 인원을 구한다.




```python
import sys

T = int(sys.stdin.readline())

for _ in range(T):

    #각 testcase를 돌 때마다 cnt, 사람수, 성적을 새로 받아줌
    cnt = 0
    n = int(sys.stdin.readline())
    people = [tuple(sys.stdin.readline().split()) for i in range(n)]

    #이중 for문을 사용해서
    for i in range(n):
        for j in range(n):
            #성적이 하나라도 1등이면, break해서 for문 더 적게 돌리기
            if people[i][0] == '1' or people[i][1] == '1':
                break
            #다른 사람의 1차 순위와 2차 순위보다 낮다면, 선발될수 없으니 cnt를 증가시키고 break
            if (people[i][0] > people[j][0]) and (people[i][1] > people[j][1]):
                cnt += 1
                break
	
    #전체 인원 n에서 선발될 수 없는 인원 cnt를 빼주기
    print(n - cnt)
```



## 문제점

시간초과가 뜸..

- 이중 for문이 문제임

- 근데 이중 for문을 안돌면서 어떻게 하나하나 비교하지? 라던 찰나에 현식님이 도움을 주심 + 선영님과 탐구

- => 순위대로 정렬 후,

  => 비교 순위를 두고 각각의 순위를 다시 비교

  

(원리는 똑같이 전체 n에서 불합격 cnt를 빼줌.)

```python
import sys

T = int(sys.stdin.readline())

for _ in range(T):

    n = int(sys.stdin.readline())
    #순위대로 정렬을 해주자.
    #people을 모두 0으로 초기화하고,
    people = [0] * (n+1)

    #첫번째 순위를 index로 주고,해당 인덱스의 value로 두번째 순위를 줌
    #첫번째 순위대로 값들이 정렬됨
    for i in range(n):
        score1, score2 = map(int, sys.stdin.readline().split())
        people[score1] = score2

    #그말은, 첫번째로 순위로 정렬되어 있으므로,
    #두번째 순위가 앞의 순위보다 크다면, 합격이 불가능
    cnt = 0
    #제일 첫 임시 값으로, 제일 첫 index의 값을 넣어줌.
    #people[0]은 0순위이므로 people[1]을 넣어줌
    temp = people[1]
    for i in range(1, n+1):
        #첫번째 순위로 정렬되므로,
        #두번째 순위가 앞의 순위보다 크다면, 합격이 불가능
        
        #그렇기에, 해당 값이 임시값보다 적거나 같으면 통과
        #그리고 temp를 더 작은 값으로 교환
        if people[i] <= temp:
            temp = people[i]
        #해당 값이 임시값보다 크다면 불합격
        #cnt 값 증가
        else:
            cnt += 1
    
    #전체 n에서 불합격 cnt를 빼줌
    print(n - cnt)
```
