# coding:utf-8

a, b = [int(x) for x in input().split(' ')]

if not abs(a - b) % 2:
    print(int(abs(a - b) / 2 + min(a, b)))
else:
    print('IMPOSSIBLE')