## [BOJ13164 / 행복 유치원]

### 문제

- N명의 원생들을 K개의 조로 나눔
- 각 조에는 원생이 적어도 한명 있으며, 같은 조의 원생들은 서로 인접함
- 각 조에서 (가장 키가 큰 원생 - 가장 키가 작은 원생)만큼 비용이 들 때, 비용의 합을 최소로 하려면 나오는 조의 개수를 출력하라.



### 내가 생각해준 방법

- 이웃과 차이값이 적게 나는 것들만 선택해주자.




### 내가 짠 코드

(원리)

- 차이값들을 저장해주고
- 차이값들이 가장 적은 것들만, 조 개수만큼 선택해준다.

```python
n, k = map(int, input().split())
heights = list(map(int, input().split()))

#이웃한 값들끼리의 차이값을 abstraction에 담아줌
abstraction = []
for i in range(1, n):
    abstraction.append(heights[i] - heights[i-1])

#abstraction을 순서대로 정렬해줌
abstraction.sort()

#그룹의 개수가 총 k개 이므로, k-1의 범위까지 앞에서부터 가져옴
result = []
for i in range(k-1):
    result.append(abstraction[i])

print(sum(result))
```



## 문제점

틀렸다고 뜸

=> 생각해보니까 그룹의 개수는 k개 이지만, 실질적으로 우리가 선택해야하는 이웃간의 차이는, n-k개 이다. 

=> 왜냐하면, 서로 이웃한 것만 뽑는 것이 아니라, 여러칸 차이나는 것을 선택할 수도 있다.

=> 즉, 총 전체 n명 중에서 그룹 개수 k 가 아닌, 그 반대인 n-k를 뽑아줘야한다.

```python
#입력값들을 받아줌
n, k = map(int, input().split())
heights = list(map(int, input().split()))

#이웃값들과의 차이값을 abstraction에 담아줌
abstraction = []
for i in range(1, n):
    abstraction.append(heights[i] - heights[i-1])

#abstraction의 값들을 크기 순으로 정렬해줌
abstraction.sort()

#abstraction이 크기 순으로 정렬되어 있으니,
#앞에서부터 n-k개만큼 result 변수에 담아줌
result = []
for i in range(n-k):
    result.append(abstraction[i])

#result 변수에 있는 수들을 모두 더해줌
print(sum(result))
```

