## [BOJ2847 / 게임을 만든 동준이]

### 문제

- 각 단계별 점수가 점점 증가한다고 할 때,

- 각 단계별 점수를 몇 번 감소시키면 되는지 구하라.

  

### 내가 생각해준 방법

- 각 단계별 숫자를 구하고, 현재의 숫자와 차이를 구해준다.




### 내가 짠 코드

(원리)

- 각 단계별 점수를 거꾸로 뒤집어서 내림차순이 되도록 한다.
- 그리고, 현재 단계와의 차이를 더해준다.

```python
import sys

input = sys.stdin.readline

#입력받기
n = int(input())
nums = [int(input()) for _ in range(n)]

#입력받은 점수를 뒤집어준다.
nums.reverse()

total = 0			#전체 감소시키는 횟수를 담아주는 변수
now = nums[0] - 1	#현재 단계가 가져야 하는 점수

#각 단계의 현재 점수에서 현재 단계가 가져야 하는 점수를 빼준다.
for i in range(1, n):
    total += (nums[i] - now)
    now -= 1

print(total)
```



## 문제점

생각해보니까 무조건 단계별 점수가 무조건 1씩 줄어드는 게 아니라, 2나 3씩 .. 줄어드는 경우도 있었다.

```python
import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.reverse()

total = 0
now = nums[0] - 1
for i in range(1, n):
		#현재 점수가 내가 가져야 하는 점수보다 적은 경우(줄일 필요가 없음)
    if nums[i] < now:
        now = nums[i]
		#현재 점수가 내가 가져야 하는 점수보다 크거나 같은 경우
    else:
        total += (nums[i] - now)
    now -= 1

print(total)
```

