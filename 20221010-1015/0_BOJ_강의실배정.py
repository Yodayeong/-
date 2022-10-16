import heapq
import sys
sys.stdin = open('0_BOJ_강의실배정.txt', 'r')

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