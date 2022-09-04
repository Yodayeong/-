## remove 함수

- array.revmore(x) 형태

- array에서 x를 삭제해줌

- 삭제하고자 하는 값이 여러개라도, 첫번째 값만 삭제해줌

- 모든 값을 삭제할 때는 for문을 이용할 수도 있음

  - ```python
    numbers = [1, 2, 2, 3, 3, 3]
    
    for _ in numbers:
        numbers.remove(3)
    print(numbers)
    ```

    

## [BOJ10546 / 배부른 마라토너]

### 문제

n개 줄에 마라톤 참가자의 이름이 입력되고

(n-1)개 줄에 마라톤 완주자의 이름이 입력된다.

참가해놓고 완주하지 못한 단 한명의 배부른 참가자를 출력해라.



### 내가 생각해준 방법

list에 append와 remove 해주고, list에 남은 한명을 출력한다.



### 내가 짠 코드

(원리)

- 참가자들을 list에 append 해준다.
- 완주자들을 list에서 remove 해준다.
- list에 남은 한명을 출력해준다.

```python
n = int(input())

#참가자 append
maratoners = []
for i in range(n):
    maratoners.append(input())

#완주자 remove
for i in range(n-1):
    maratoners.remove(input())

#배부른 마라토너 출력
print(*maratoners)
```



## 문제점

시간초과가 뜸



## sys.stdin.readline()

반복문으로 여러 줄을 입력받을 때 input()을 써주면 시간초과가 발생할 수 있다.

그러나 sys.stdin.readline()은 한 줄 단위로 입력받기에, 개행문자가 같이 입력됨.

- 정수를 입력받을 때

  => a = **int**(sys.stdin.readline())

- 문자열을 입력받을 때

  => a = sys.stdin.readline().rstrip()



## 문제점

그래도 시간초과가 뜸



**리스트의 경우에는 시간이 자료의 크기에 비례하여 늘어나지만, 딕셔너리는 거의 일정한 시간으로 탐색 완료** 라는 점을 활용

=> 딕셔너리를 사용해서 풀자!



(원리)

- 딕셔너리에 참가자들과 그 수를 입력받는다.
- 완주한 참가자들은 수를 -1 해준다.
- 결국 완주하지 못한 참가자 한명만 수가 1일 것이고, 나머지는 0일 것이다.

```python
n = int(input())

#참가자들과 그 수를 입력받기
maratoners = dict()
for i in range(n):
    maratoner = input()

    if maratoner in maratoners:
        maratoners[maratoner] += 1
    else:
        maratoners[maratoner] = 1

#완주자들은 수를 -1해주기
for i in range(n-1):
    completed = input()

    if maratoner in maratoners:
        maratoners[completed] -= 1

#결국 dictionary에서 수가 1인 참가자만 출력
for i in maratoners:
    if maratoners[i] == 1:
        print(i)
```
