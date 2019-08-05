# coding:utf-8
n = int(input())
num_list = [int(x) for x in input().split(' ')]

diff_list = []
for i, num in enumerate(num_list):
    if not i+1 == num:
        diff_list.append([i+1, num])
    if len(diff_list) > 2:
        break
if len(diff_list) == 2 and diff_list[0][0] == diff_list[1][1] and diff_list[0][1] == diff_list[1][0]:
    print('YES')
elif len(diff_list) == 0:
    print('YES')
else:
    print('NO')