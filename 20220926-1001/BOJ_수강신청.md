## [BOJ13414 / 수강신청]

### 문제

- 수강 신청 버튼을 먼저 클릭한 사람이 대기열에 먼저 들어감
- 수강 신청 버튼을 다시 클릭한 사람은 대기열의 맨 마지막에 다시 추가됨
- 수강신청이 끝나면, 가장 맨 앞의 학생부터 인원 수 만큼 자동 수강신청됨



### 내가 생각해준 방법

- 중복되는 사람 제거 및 수강인원만큼 앞에서부터 출력




### 내가 짠 코드

(원리)

- set 자료형을 활용하여 중복되는 수 제거
- 그 후, 수강 인원만큼 앞에서부터 출력



## 문제

생각해보니 set 자료형은 순서가 없어서 적용하고 나면 순서가 뒤섞인다.



=> 딕셔너리 자료형을 활용하자!

- 저장해줄때, 딕셔너리 자료형으로 저장을 해주는데,
  - 중복되는 사람이 있다면, 그 자리에서 del 해주고 다시 추가
- 다 추가 된 후에는, 앞에서부터 수강인원 만큼 끊자

```python
import sys

#수강인원과 신청인원을 받아줌
total, n = map(int, input().split())

#딕셔너리 형태로 신청한 사람들을 받아줌
people_list = dict()
for i in range(n):
    person = sys.stdin.readline().rstrip()

    #근데 이미 나와 중복되는 사람이 있다면,
    if person in people_list:
        #del 해주고 다시 추가
        del(people_list[person])
        people_list[person] = 1
    #그게 아니면,
    else:
        #그냥 추가
        people_list[person] = 1

cnt = 0
for people in people_list:
    #수강인원에 도달하기 전까지
    if cnt == total:
        break
    #앞에서부터 사람 출력
    print(people)
    cnt += 1
```
