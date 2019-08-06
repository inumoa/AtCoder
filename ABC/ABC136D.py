# coding:utf-8

rl_list = input()

num_list = []

# rightフラグ 最初はrightなので初期値True
r_f = True
# leftフラグ
l_f = False

count = 0
temp = []
for i, rl in enumerate(rl_list):
    if r_f:
        if rl == 'R':
            count += 1
        else:
            temp = [count]
            r_f = False
            l_f = True
            count = 1
    elif l_f:
        if rl == 'R':
            temp.append(count)
            num_list.append(temp)
            r_f = True
            l_f = False
            count = 1
        else:
            count += 1
temp.append(count)
num_list.append(temp)

result = ''
for num in num_list:
    result += '0 ' * (num[0] - 1) + str(-(-num[0] // 2) + num[1] // 2) + ' ' + str(num[0] // 2 + -(-num[1] // 2)) + ' ' + '0 ' * (num[1] - 1)

print(result[:-1])
