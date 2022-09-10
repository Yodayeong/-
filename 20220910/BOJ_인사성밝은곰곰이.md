## [BOJ25192 / 인사성 밝은 곰곰이]

### 문제

- 'Enter'가 입력될 때 마다 새로운 톡방
- 그 후로 닉네임들이 입력된다.
- 닉네임이 첫번째로 입력될 때는 무조건 곰곰티콘을 사용한다.
- 그 이후부터는 평범한 채팅기록이다.
- 이때, 각 톡방 별로 사용된 곰곰티콘의 개수를 구하라.



### 내가 생각해준 방법

- 리스트를 활용하여, 'Enter'가 입력될 때마다 새로운 멤버 리스트를 생성한다.



### 내가 짠 코드

(원리)

- 'Enter'가 입력되면 새로운 리스트 생성
- 그것이 아니라면,
  - 입력 멤버가 리스트에 없다면, 리스트에 추가해주고 cnt 증가
  - 입력 멤버가 리스트에 이미 있다면, 아무것도 해주지 않음




```python
T = int(input())

cnt = 0
members = []
for _ in range(T):
    temp = input()

    if temp == 'ENTER':
        members = []
    else:
        if temp not in members:
            cnt += 1
            members.append(temp)

print(cnt)
```



## 문제점

시간 초과 발생

=> 리스트 보다 시간 복잡도가 적은 딕셔너리를 활용!

=> 입력값을 받을 때 sys.stdin.readline() 활용!

```python
import sys

T = int(sys.stdin.readline())

cnt = 0
members = dict()
for _ in range(T):
    temp = sys.stdin.readline().rstrip()

    if temp == 'ENTER':
        members = dict()
    else:
        if temp not in members:
            cnt += 1
            members[temp] = 1

print(cnt)
```

