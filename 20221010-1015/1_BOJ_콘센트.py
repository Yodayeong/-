import heapq
import sys
sys.stdin = open('1_BOJ_콘센트.txt', 'r')

N, M = map(int, input().split())
time = list(map(int, input().split()))
#시간을 내림차순 정렬 해야함
time.sort(reverse=True)

#콘센트 개수만큼 리스트를 만들어줌
time_list = [0] * M
#time_list를 heap으로 만들어줌
heapq.heapify(time_list)

#heapq는 min heap으로 구현이 되고,
#heapq.heappop을 하면, 가장 작은 원소가 튀어나옴
for t in time:
    #가장 크기가 적은 콘센트에 계속해서 더해나가준다.
    heapq.heappush(time_list, heapq.heappop(time_list) + t)

#콘센트 중 크기가 가장 큰 것을 출력
print(max(time_list))