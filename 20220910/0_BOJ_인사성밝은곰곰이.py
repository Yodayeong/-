import sys
sys.stdin = open('0_BOJ_인사성밝은곰곰이.txt', 'r')

T = int(sys.stdin.readline())

cnt = 0
members = dict()
for _ in range(T):
    temp = sys.stdin.readline().rstrip()

    if temp == 'ENTER':
        members = dict()
    else:
        if temp not in members:
            cnt += 1
            members[temp] = 1

print(cnt)