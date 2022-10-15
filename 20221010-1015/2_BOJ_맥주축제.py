import heapq
import sys
sys.stdin = open('2_BOJ_맥주축제.txt', 'r')

period, satisfy, beer_type = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(beer_type)]

min_heap = []
heapq.heapify(min_heap)

for i in range(beer_type-1):
    now_beer = beers[0+i:period-1+i]

    now_beer_total = 0
    for beer in now_beer:
        now_beer_total += beer[0]
    print(now_beer_total)
    
    j = period-1+i
    while j <= beer_type-1:
        print(j, now_beer_total + beers[j][0], max(beers[0+i][1], beers[period-2+i][1], beers[j][1]))
        if now_beer_total + beers[j][0] >= satisfy:
            heapq.heappush(min_heap, max(beers[0+i][1], beers[period-2+i][1], beers[j][1]))
        j += 1

print(heapq.heappop(min_heap))