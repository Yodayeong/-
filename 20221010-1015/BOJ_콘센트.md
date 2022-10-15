## [BOJ23843 / 콘센트]

### 문제

- **전자기기**: N개, **콘센트**: M개, **충전시간**: 2의 k 제곱
- 충전 최소 시간은?

### 내가 생각해준 방법

- 그때 그때 총값이 가장 적은 곳에다가 값을 붙여넣어주자!




### 내가 짠 코드

(원리)

- 각 단계에서 총합이 가장 적은 곳에다가 값을 붙여줌
- 이때, time을 내림차순으로 정렬해야 올바른 값이 나옴

```python
N, M = map(int, input().split())
time = list(map(int, input().split()))
time.sort(reverse=True)	#시간을 내림차순 정렬 해야함

#콘센트 개수만큼 리스트를 만들어줌
time_list = [[0] for _ in range(M)]

for t in time:
    check = 0
    minest = sum(time_list[0])

    #총합이 가장 적은 곳을 체크해줌
    for i in range(M):
        if sum(time_list[i]) < minest:
            minext = sum(time_list[i])
            check = i
    
    #체크된 콘센트에 값을 추가해줌
    time_list[check].append(t)

#콘센트 들 중, 총합이 가장 큰 곳을 찾아서
max = 0
for i in range(M):
    if sum(time_list[i]) > max:
        max = sum(time_list[i])
        
#print 해줌
print(max)
```



## heap으로 구현

```python
import heapq

N, M = map(int, input().split())
time = list(map(int, input().split()))
#시간을 내림차순 정렬 해야함
time.sort(reverse=True)

#콘센트 개수만큼 리스트를 만들어줌
time_list = [0] * M
#time_list를 heap으로 만들어줌
heapq.heapify(time_list)

#heapq는 min heap으로 구현이 되고,
#heapq.heappop을 하면, 가장 작은 원소가 튀어나옴
for t in time:
    #가장 크기가 적은 콘센트에 계속해서 더해나가준다.
    heapq.heappush(time_list, heapq.heappop(time_list) + t)

#콘센트 중 크기가 가장 큰 것을 출력
print(max(time_list))
```



