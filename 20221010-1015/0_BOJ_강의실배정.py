import heapq
import sys
sys.stdin = open('0_BOJ_강의실배정.txt', 'r')

import heapq

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
            break

print(classrooms)
#교실의 개수 출력
print(len(classrooms))
