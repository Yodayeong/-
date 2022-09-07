## Heap

- heapq 모듈은 이진트리 기반의 최소 힙(min heap) 자료구조를 제공

- min heap을 사용하면,

  - 원소들이 항상 정렬된 상태로 추가 및 삭제
  - min heap에서 가장 작은 값은 인덱스 0에 위치

- heapq.heappush : 원소 추가

- heapq.heappop : 원소 삭제

- ```python
  import heapq
  
  nums = [1, 2, 3, -1, 1]
  heapq.heapify(nums)
  heapq.heappop(nums)
  heapq.heappush(num, 10)
  ```



## [BOJ11286 / 절댓값 힙]

### 문제

- 0이 아닌 정수가 주어지면, 배열에 x라는 값을 저장한다.
- 0이 주어지면, 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

- 단, 절댓값이 가장 작은 값이 여러개일때는 가장 작은 수를 출력 및 제거한다.
- 만약 배열이 비어있는 경우인데 값을 출력하라고 한 경우에는 0을 출력한다.



### 내가 생각해준 방법

값을 자동으로 정렬해주는 min heap을 활용한다.



### 내가 짠 코드

(원리)

- 입력이 정수인 경우
  - 절댓값과 원래 수를 튜플로 묶어서 배열에 저장한다.

- 입력이 0인 경우
  - 만약 heap이 비어있는 경우
    - 0을 출력

  - 그렇지 않으면
    - heappop

```python
import heapq

n = int(input())

min_heap = []
for i in range(n):
    value = int(input())
	
    #입력값이 정수라면,
    if value != 0:
        heapq.heappush(min_heap, (abs(value), value))
        
    #입력값이 0이라면,
    else:
        #heap이 비어있다면,
        if len(min_heap) == 0:
            print('0')
        #heap이 비어있지 않다면,
        else:
            print(heapq.heappop(min_heap)[1])
```



## 문제점

시간초과

=> 파일 읽어오는 방식을 변화해주자!

```python 
#input() 방식을 sys.stdin.readline()으로 변경
n = int(sys.stdin.readline())

min_heap = []
for i in range(n):
    #input() 방식을 sys.stdin.readline()으로 변경
    value = int(sys.stdin.readline())

    if value != 0:
        heapq.heappush(min_heap, (abs(value), value))
    else:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap)[1])
```

