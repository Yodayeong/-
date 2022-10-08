## [BOJ2012 / 등수 매기기]

### 문제

- 모든 학생들은 자신의 예상 등수를 매김
- A등으로 예상 했는데, B등으로 나온다면, 이 사람의 불만도는 |A - B|
- N명의 사람들의 불만도의 총합을 최소화 해주자.



### 내가 생각해준 방법

- 중복되는 등수를 따로 저장해, 아직 나오지 않은 등수와의 차이값을 구해줌




### 내가 짠 코드

(원리)

- 등수를 모두 0으로 초기화 후,
- 등수가 나오면 1로 체크해준다.
- 자신과 중복되는 친구가 있으면 left에 담아주고,
- 이후에 남은 등수와의 차이값을 구해준다.

```python
import sys

input = sys.stdin.readline

n = int(input())
ranks = [int(input()) for _ in range(n)]

#초기 등수들을 visited로 두고 모두 0으로 초기화해줌
visited = [0 for _ in range(n+1)]

#등수가 나올때마다
#처음 나온 등수라면, visited를 체크해주고
#이미 나온 등수라면(visited가 체크되어 있으면), left에 담아줌
left = []
for rank in ranks:
    if visited[rank] == 0:
        visited[rank] = 1
    else:
        left.append(rank)

#자신과 가장 이웃한 친구들과 비교해야하니까(순서대로 비교), sort 해줌
left.sort()

#앞에서부터 아직 안나온 등수가 있다면, 
#left의 친구와 차이값을 구해서 total에 더해줌
total = 0
left_temp = 0
for i in range(1, n+1):
    if visited[i] == 0:
        total += (abs((i) - left[left_temp]))
        left_temp += 1

print(total)
```



## 문제점

계속 45%에서 틀렸다고 함....

그냥 똑같은 원리로 앞에서부터 비교해줌..

```python
import sys

input = sys.stdin.readline

n = int(input())
ranks = [int(input()) for _ in range(n)]

#등수를 오름차순 정렬해주고
ranks.sort()

#자신과 가장 인접한 등수와의 차이를 구해줌
total = 0
for i in range(1, n+1):
    total += abs((i - ranks[i-1]))

print(total)
```



