import sys
sys.stdin = open('1_BOJ_수강신청.txt', 'r')

total, n = map(int, input().split())

people_list = dict()
for i in range(n):
    person = sys.stdin.readline().rstrip()

    if person in people_list:
        del(people_list[person])
        people_list[person] = 1
    else:
        people_list[person] = 1

cnt = 0
for people in people_list:
    if cnt == total:
        break
    print(people)
    cnt += 1