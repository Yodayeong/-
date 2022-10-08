import sys
sys.stdin = open('1_BOJ_배.txt', 'r')

crane = int(sys.stdin.readline().rstrip())
weight_limit = list(map(int, input().split()))
box = int(sys.stdin.readline().rstrip())
box_weight = list(map(int, input().split()))

weight_limit.sort(reverse=True)
box_weight.sort(reverse=True)

cnt = 0
idx = []
if box_weight[0] > weight_limit[0]:
    print(-1)
else:
    while True:
        if box == 0:
            print(cnt)
            break

        if box < crane:
            for i in range(box):
                if weight_limit[i] >= box_weight[i]:
                    idx.append(i)
        if box > crane:
            for i in range(crane):
                if weight_limit[i] >= box_weight[i]:
                    idx.append(i)

        idx.sort(reverse=True)

        for i in idx:
            box_weight.pop(i)
        box -= len(idx)

        idx = []
        cnt += 1
