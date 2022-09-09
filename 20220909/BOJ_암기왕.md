## [BOJ2776/ 암기왕]

### 문제

수첩2에 적힌 M개 각각의 숫자가 수첩1에 적혀있으면 1출력, 적혀있지 않으면 0 출력



### 내가 생각해준 방법

수첩2를 순서대로 돌아가면서 수첩1에 있으면 1출력, 아니면 0 출력



### 내가 짠 코드

(원리)

- for문을 사용해서 수첩2의 숫자들을 하나하나 확인해주자.



```python
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    note_1 = list(map(int, sys.stdin.readline()))
    
    m = int(sys.stdin.readline())
    note_2 = list(map(int, sys.stdin.readline()))
    
    #수첩2의 숫자들을 돌면서
    for num in note_2:
        #수첩1에도 있다면,
        if num in note_1:
            print('1')
        #수첩1에 없다면,
        else:
            print('0')
```



## 문제점

시간 초과



## set 자료형

- 순서가 없고, 집합 안에서는 unique한 값을 가짐

  => 중복되는 원소가 없다.



- 수첩1의 숫자들을 중복 제거하여, 숫자가 있는지 확인하는 시간을 줄인다.

  ```python
  import sys
  
  T = int(sys.stdin.readline())
  
  for i in range(T):
      n = int(sys.stdin.readline())
      #set 자료형으로 중복되는 수들을 제거해준다.
      note_1 = set(map(int, sys.stdin.readline().split()))
      
      m = int(sys.stdin.readline())
      note_2 = list(map(int, sys.stdin.readline().split()))
  
      for num in note_2:
          if num in note_1:
              print('1')
          else:
              print('0')
  ```

  

  
