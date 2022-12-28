import sys
sys.stdin = open('0_BOJ_N과M.txt', 'r')

N, M = map(int, input().split())

visited = []

def back():
    if len(visited) == M:
        print(" ".join(map(str, visited)))
        return
    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            back()
            visited.pop()

back()