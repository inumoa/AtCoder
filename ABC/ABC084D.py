Q = int(input())
lr_list = [list(map(int, input().split())) for _ in range(Q)]

max_val = max([lr[1] for lr in lr_list])

# エラトステネスの篩
num_list = list(range(max_val + 1))
for num in num_list[2:max_val // 2 + 1]:
    if num > 0:
        for i in range(num*2, max_val+1, num):
            num_list[i] = -1

prime_num_set = set([num for num in num_list if num>0][1:])

# 累積和
sum_list = [0, 0, 0]
for i in range(3, max_val+1):
    if i in prime_num_set and (i+1)//2 in prime_num_set:
        sum_list.append(sum_list[-1]+1)
    else:
        sum_list.append(sum_list[-1])

for l, r in lr_list:
    print(sum_list[r] - sum_list[l-1])