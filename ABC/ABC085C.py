# coding:utf-8

n, y = [int(x) for x in input().split(' ')]

# 表示済みふらぐ
f = False

for i in range(n+1):
    for j in range(n-i+1):
        if 10000*i + 5000*j > y:
            break
        elif 10000*i + 5000*j + 1000*(n-i-j) == y:
            print('{} {} {}'.format(i, j, n-i-j))
            f = True
            break
    if f:
        break

if not f:
    print('-1 -1 -1')