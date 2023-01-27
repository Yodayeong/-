import sys
sys.stdin = open('0_BOJ_1,2,3더하기2.txt', 'r')

n, k = map(int, input().split())

sum_list = []
def recursive_function(temp_list):
    if sum(temp_list) == n:
        sum_list.append(temp_list)
        return

    if sum(temp_list)+1 <= n:
        recursive_function(temp_list + [1])

    if sum(temp_list)+2 <= n:
        recursive_function(temp_list + [2])
    
    if sum(temp_list)+3 <= n:
        recursive_function(temp_list + [3])

recursive_function([])

if len(sum_list) < k:
    print(-1)
else:
    print(*sum_list[k-1], sep='+')