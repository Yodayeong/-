## [BOJ1351 / 무한 수열]

### 문제

- ⌊x⌋는 x를 넘지 않는 가장 큰 정수임
- 무한 수열 A는 다음과 같다.
  - A0 = 1
  - Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
- N, P와 Q가 주어질 때, AN을 구하는 프로그램을 작성하라.



### 내가 생각해준 방법

- 리스트에 n번째 값들을 저장해줌
- 각 단계별 계산 후 필요한 값들을 꺼내옴




### 내가 짠 코드

(원리)

- 

```python
n, p, q = map(int, input().split())

values = [1, ]
for i in range(1, n+1):
    first = int(i/p)
    second = int(i/q)

    values.append(values[first] + values[second])

print(values[n])
```
