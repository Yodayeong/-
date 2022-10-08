## [BOJ1092 / 배]

### 문제

- 크레인 N대 
  - 모든 크레인은 동시에 움직임/무게제한보다 무거운 박스는 옮길 수 없음

- 1분에 박스를 하나씩 옮길 수 있음
- 모든 박스를 옮기는데 드는 시간의 최솟값을 구하라
- 단, 모든 박스를 배로 옮길 수 없으면 -1 출력



### 내가 생각해준 방법

- deque를 활용해주자.




### 내가 짠 코드

(원리)

- 우선, crane과 box_weight을 내림차순으로 정렬한다.
- 앞에서부터 옮길 수 있는 크기라면, 옮겨준다. (deque의 popleft 활용)

```python
from collections import deque

#입력값 다 받아줌
crane = int(input())
weight_limit = list(map(int, input().split()))
box = int(input())
box_weight = list(map(int, input().split()))

#내림차순으로 정렬해줌
weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)

#box_weight_list에서 pop을 해야하므로, deque로 만들어줌
box_weight_list = deque(box_weight)

cnt = 0
temp = 0
#상자를 모두 옮기지 못한다면, -1 출력
if box_weight_list[0] > weight_limit[0]:
    print(-1)
else:
    #무한 반복을 하는데,
    while True:
        #더 이상 옮길 박스가 없다면, cnt를 출력해주고 break
        if box == 0:
            print(cnt)
            break
            
        #crane의 개수보다 box의 개수가 적다면,
        if box < crane:
            for i in range(box):
                if weight_limit[i] >= box_weight_list[i]:
                    temp += 1
            box -= temp
        #crane의 개수가 box의 개수보다 많다면,
        else:
            for i in range(crane):
                if weight_limit[i] >= box_weight_list[i]:
                    temp += 1
            box -= temp
        for j in range(temp):
            box_weight_list.popleft()
        temp = 0
        cnt += 1
```



## 문제점

생각해보니까 앞에서부터 비교하면서, crane의 크기가 더 크면 끊지 않아도,

뒤에 있는 박스가 먼저 옮겨질 수도 있다는 사실을 알았다.

```python
#값들을 받아줌
crane = int(input())
weight_limit = list(map(int, input().split()))
box = int(input())
box_weight = list(map(int, input().split()))

#크레인의 무게제한과 박스들의 무게를 내림차순으로 정렬해줌
weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)

cnt = 0		#마지막에 출력할 이동 횟수
idx = []	#각 이동 회차마다, 이동해야 할 박스의 인덱스

#박스를 모두 옮기지 못하면, -1 출력
if box_weight[0] > weight_limit[0]:
    print(-1)
#그렇지 않다면,
else:
    #무한 반복을 하는데
    while True:
        #더 이상 옮길 박스가 없으면, 이동 횟수 출력 및 break
        if box == 0:
            print(cnt)
            break

        #box 수보다 crane의 개수가 더 많은 경우
        if box < crane:
            for i in range(box):
                if weight_limit[i] >= box_weight[i]:
                    idx.append(i)
        #box 수가 crane의 개수보다 많은 경우
        if box > crane:
            for i in range(crane):
                if weight_limit[i] >= box_weight[i]:
                    idx.append(i)

        #앞에서부터 박스를 제거하면 한칸씩 당겨지므로 idx 내림차순 정렬
        idx.sort(reverse=True)

        #해당 idx의 박스들을 pop 해줌
        for i in idx:
            box_weight.pop(i)
        #제거한 박스 수만큼 박스 개수 줄여줌
        box -= len(idx)

        #매 회차마다 idx 초기화 및, cnt 증가
        idx = []
        cnt += 1
```

