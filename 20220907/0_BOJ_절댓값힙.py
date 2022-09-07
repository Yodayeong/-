import heapq
import sys
sys.stdin = open('0_BOJ_절댓값힙.txt', 'r')

n = int(sys.stdin.readline())

min_heap = []
for i in range(n):
    value = int(sys.stdin.readline())

    if value != 0:
        heapq.heappush(min_heap, (abs(value), value))
    else:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap)[1])