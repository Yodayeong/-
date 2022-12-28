## 백트래킹

- 참고사이트 : https://veggie-garden.tistory.com/24



## [BOJ15649 / N과 M (1)]

### 문제

- 자연수 N과 M이 주어졌을 때, 
  - 1부터 N까지 자연수 중에서
  - 중복 없이 M개를 고른 수열




### 내가 생각해준 방법

- ![KakaoTalk_20221111_010348994](BOJ_N과M(1).assets/KakaoTalk_20221111_010348994.jpg)

  

### 내가 짠 코드

(원리)

- 

```python
import sys
sys.stdin = open('0_BOJ_N과M.txt', 'r')

N, M = map(int, input().split())

visited = []

def back():
    if len(visited) == M:
        print(" ".join(map(str, visited)))
        return
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            back()
            visited.pop()

back()
```



- Permutations 
- Unpacking : 리스트 하나씩 출력? * : 띄어쓰기도 됨
