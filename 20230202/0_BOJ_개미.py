import sys
sys.stdin = open('0_BOJ_개미.txt', 'r')

n, m = map(int, input(). split())

list_n = list(input())
list_m = list(input())
list_n.reverse()

T = int(input())

initial = list_n + list_m

for i in range(T):
    if i >= n+m:
        break

    start = n-1-i
    end = n+i
    
    while(start < end):
        initial[start], initial[start+1] = initial[start+1], initial[start]
        start += 2

    if i > n:
        start = -n+i
        end = 