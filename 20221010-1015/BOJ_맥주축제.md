## [BOJ17503 / 맥주 축제]

### 문제

- 

### 내가 생각해준 방법

- 만족도가 넘는 것들의 도수를 min heap에 추가

  - min heap의 길이가 0이면, -1 출력 

  - min heap의 길이가 0이 아니라면, 도수 중, 가장 적은 것을 pop

    



### 내가 짠 코드

(원리)

- 

```python
import heapq

period, satisfy, beer_type = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(beer_type)]

#만족도가 넘은 것들의 도수 값을 담아줄 min_heap 생성
min_heap = []
heapq.heapify(min_heap)

for i in range(beer_type-1):
    now_beer = beers[0+i:period-1+i]

    now_beer_total = 0
    for beer in now_beer:
        now_beer_total += beer[0]
    print(now_beer_total)
    
    j = period-1+i
    while j <= beer_type-1:
        print(j, now_beer_total + beers[j][0], max(beers[0+i][1], beers[period-2+i][1], beers[j][1]))
        if now_beer_total + beers[j][0] >= satisfy:
            heapq.heappush(min_heap, max(beers[0+i][1], beers[period-2+i][1], beers[j][1]))
        j += 1

print(heapq.heappop(min_heap))
```
