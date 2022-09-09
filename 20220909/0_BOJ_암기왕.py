import sys
sys.stdin = open('0_BOJ_암기왕.txt', 'r')

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    note_1 = set(map(int, sys.stdin.readline().split()))
    
    m = int(sys.stdin.readline())
    note_2 = list(map(int, sys.stdin.readline().split()))

    for num in note_2:
        if num in note_1:
            print('1')
        else:
            print('0')