# coding:utf-8

n = int(input())
town_list = [int(x) for x in input().split(' ')]
saver_list = [int(x) for x in input().split(' ')] + [0]

count = 0

for i, town in enumerate(town_list):
    if town_list[i] >= saver_list[i]:
        count += saver_list[i]
    else:
        count += town_list[i]
        if not i+1 == len(saver_list):
            count += min(town_list[i+1], saver_list[i] - town_list[i])
            town_list[i+1] = max(town_list[i+1] - (saver_list[i] - town_list[i]), 0)

print(count)