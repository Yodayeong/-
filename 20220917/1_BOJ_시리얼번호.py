import sys
sys.stdin = open('1_BOJ_시리얼번호.txt', 'r')

n = int(input())
guitars = [input() for _ in range(n)]

len_serial = []
for guitar in guitars:
    if len(guitar) not in len_serial:
        len_serial.append(len(guitar))
len_serial.sort()

