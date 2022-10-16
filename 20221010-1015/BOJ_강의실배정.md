## [BOJ11000 / 강의실 배정]

### 문제

- Si에 시작해서 Ti에 끝나는 N개의 수업
- 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 함
- 이때, 수업이 끝난 직후에 바로 다음 수업을 시작할 수 있음



### 내가 생각해준 방법

- 최대 힙(max heap)을 활용해주자!




### 내가 짠 코드

(원리)

- 최대 힙으로 구현을 하여, 
- 현재 내 시간이 어떤 교실과 겹치지 않는다면,
  - 겹치지 않는 교실에 heappush를 해주고

- 모든 수업과 겹친다면,
  - 새로운 교실을 연다.


```python
import heapq

n = int(input())

class_list = []

#첫 시간을 입력받아서 heap에 미리 하나 push 해둔다.
first_time = []
time_start, time_end = map(int, input().split())
for time in range(time_start, time_end+1):
    first_time.append(-time)
heapq.heapify(first_time)
class_list.append(first_time)

#첫 시간이 하나 들어있으므로, n-1만큼 for문을 돌아준다.
for i in range(n-1):
    #수업 시작 시간과 끝나는 시간을 입력받고,
    time_start, time_end = map(int, input().split())

    #교실들을 돌면서,
    #각 교실의 끝나는 시간(최대 힙)과 내 수업 시작 시간을 비교
    for items in class_list:
        #만약 시간이 겹치지 않는다면,
        if -time_start <= items[0]:
            #해당 교실에 push하고
            for time in range(time_start, time_end+1):
                heapq.heappush(items, -time)
            #break
            break
        #모든 수업과 시간이 겹친다면,
        else:
            #새로운 교실을 만든다.
            temp = []
            for time in range(time_start, time_end+1):
                temp.append(-time)
            heapq.heapify(temp)
            class_list.append(temp)
            break

#교실의 개수 출력
print(len(class_list))
```



## 문제점

- 메모리 초과 뜸

- 또 생각한 문제점이, 강의실 시간이 뒤쪽에 붙을 수도 있지만, 앞쪽에 붙을 수도 있지 않나?

```python
import heapq
import sys
sys.stdin = open('0_BOJ_강의실배정.txt', 'r')

input = sys.stdin.readline

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]
#입력받은 시간들을 오름차순으로 정렬
times.sort()

#classrooms 변수에 교실의 개수 저장
classrooms = [[0] * 1]

#시간들을 돌면서
for time in times:
    for classroom in classrooms:
        #자신의 시작시간과 교실의 끝나는 시간이 안 겹치는 곳이 있다면,
        if classroom[0] >= -time[0]:
            #해당 교실에 자신의 끝나는 시간 heappush
            heapq.heappush(classroom, -time[1])
            break
    #자신의 시작시간과 모든 교실의 끝나는 시간이 겹친다면,
    else:
        #새로운 교실을 열어줌
        new_class = [-time[1]]
        heapq.heapify(new_class)
        classrooms.append(new_class)

#교실의 개수 출력
print(len(classrooms))
```



## 또 문제점..

시간초과뜸 ....

이중 for문 때문..... 이겠지? ㅜ

=> max heap 말고 min heap으로 구현

```python
import sys
import heapq

input = sys.stdin.readline

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]
#입력받은 시간들을 오름차순으로 정렬
times.sort()

#classrooms 변수에 교실들을 저장
classrooms = []

heapq.heappush(classrooms, times[0][1])

for i in range(1, n):
    #가장 일찍 끝나는 곳보다 시간이 더 빨리 시작한다면,
    # => 모든 교실과 겹친다.
    if classrooms[0] > times[i][0]:
        new_class = times[i][1]
        heapq.heappush(classrooms, new_class)
    #그렇지 않은 경우에는,
    #어짜피 times를 sort 해놓았으니까 앞에서부터 대체해주면 된다.
    else:
        heapq.heapreplace(classrooms, times[i][1])

print(len(classrooms))
```

