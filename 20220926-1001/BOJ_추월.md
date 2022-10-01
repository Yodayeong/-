## [BOJ2002 / 추월]

### 문제

- n대의 차들이 터널 안으로 들어감
- 차들이 터널에 들어간 순서대로 적힌 리스트와, 터널에서 나온 순서대로 적힌 리스트가 있을 때
- 반드시 추월 했을 것으로 여겨지는 차들의 개수를 구하라.



### 내가 생각해준 방법

- 아래에서 부터 들어온 리스트와 나온 리스트를 비교하는데,
- 내 위치 이하에 있으면, 추월당한 것
- => 해당 차가 해당 차가 들어간 위치보다 높은 곳에 있으면 반드시 추월한 것




### 내가 짠 코드

(원리)

- 각 차들이 자신이 들어간 위치보다 높은 곳에 있으면 cnt 1 증가

```python
import sys

#n, input, output을 입력받음
n = int(sys.stdin.readline())
input = [sys.stdin.readline().rstrip() for _ in range(n)]
output = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for i in range(n):
    #자신의 위치보다 높은 곳에 있다면 cnt 증가
    if input[i] in output[:i]:
        cnt += 1

print(cnt)
```



## 문제점

생각해보니까 반드시 추월한 차여도, 자신이 들어간 위치와 같거나 그 아래인 경우가 있었다.

=> 나보다 앞에 있던 차가 나보다 아래에 있으면 된다!

```python
import sys

#n, input(들어간 순서), output(나간 순서)을 받아줌
n = int(sys.stdin.readline())
input = [sys.stdin.readline().rstrip() for _ in range(n)]
output = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for i in range(n):
    #해당 차보다 앞에 있던 차들
    prior_cars = input[:i]

    #나왔을때 해당 차의 위치
    now = output.index(input[i])

    #해당 차의 앞에 있던 차가 단 하나라도 해당 차의 뒤에 있으면
    #cnt 1증가 및 break
    for car in prior_cars:
        if car in output[now:]:
            cnt += 1
            break

print(cnt)
```



