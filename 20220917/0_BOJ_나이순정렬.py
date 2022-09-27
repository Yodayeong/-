import sys
sys.stdin = open('0_BOJ_나이순정렬.txt', 'r')

n = int(sys.stdin.readline())
people = [tuple(sys.stdin.readline().split()) for _ in range(n)]

people.sort(key = lambda x:int(x[0]))

for person in people:
    print(*person)