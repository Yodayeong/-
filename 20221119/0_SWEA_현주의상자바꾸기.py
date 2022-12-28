import sys
sys.stdin = open('0_SWEA_현주의상자바꾸기.txt', 'r')

T = int(input())

for i in range(T):
    N, Q = map(int, input().split())

    boxes = [0]*N
    for j in range(Q):
        start, end = map(int, input().split())
        for _ in range(start-1, end):
            boxes[_] = j+1
        
    print(f'#{i+1}', *boxes)