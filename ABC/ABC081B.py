#coding:utf-8

_ = input()
a_list = input().split(' ')

count_list = []

for a in a_list:
    count = 0
    a = int(a)
    while not a % 2:
           count += 1
           a = a/2
    count_list.append(count)
print(min(count_list))