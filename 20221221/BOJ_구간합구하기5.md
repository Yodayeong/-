## [BOJ11660 / 구간 합 구하기 5]

### 문제

- N×N개의 수가 N×N 크기의 표에 채워져 있을 때,  (x1, y1)부터 (x2, y2)까지 합을 구하라.

  



### 내가 생각해준 방법

- y값의 범위에 해당하는 값들이 이차원 배열의 앞자리에 해당하고
- x값의 범위에 해당하는 값들이 이차원 배열의 뒷자리에 해당함




### 내가 짠 코드

(원리)

- 해당 범위의 값들을 다 더해서 출력해줌

```python
import sys

sys.stdin = open('1_BOJ_구간합구하기5.txt', 'r')

N, M = map(int, input().split())
array_N = [input().split() for _ in range(N)]
array_M = [input().split() for _ in range(M)]

for i in range(M):
    sum = 0

    for j in range(int(array_M[i][1])-1, int(array_M[i][3])):
        for k in range(int(array_M[i][0])-1, int(array_M[i][2])):
            sum += int(array_N[j][k])

    print(sum)
```

=> 딱 봐도 시간초과가 날 것 같았음..



## 부분합과 누적합

새로운 배열을 생성해서 부분합과 누적합을 저장하여, 이를 꺼내 쓰면 시간초과를 줄일 수 있다.



#### 1차원 배열

- arr : 2  4  1  -5  2  -3

- sum : 0  2  6  7  2  4  1

- ex) sum(2, 4) = sum[4] - sum[1]
- 왜냐하면, (1~4)까지 더한 합에서 (1~1)까지 더한 합을 빼줘야 (2~4)까지 더한 합을 구할 수 있다.



#### 2차원 배열

- 1차원 배열과 마찬가지로, 

