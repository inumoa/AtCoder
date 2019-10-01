<<<<<<< HEAD
# coding:utf-8

_ = int(input())
h_list = [int(x) for x in input().split(' ')]

# 2回連続で-1の手順を適用しないといけない場合はアウト
# -1手順適用フラグ
big_f = False

no_f = False

for i, h in enumerate(h_list[:-1]):
    left = h_list[i]
    right = h_list[i+1]
    if left < right:
        big_f = False
        continue
    elif left == right:
        continue
    elif left - right == 1:
        if big_f:
            no_f = True
            break
        else:
            big_f = True
    elif left - right >= 2:
        no_f = True
        break

if no_f:
    print('No')
else:
    print('Yes')
=======
# coding:utf-8

_ = int(input())
h_list = [int(x) for x in input().split(' ')]

# 2回連続で-1の手順を適用しないといけない場合はアウト
# -1手順適用フラグ
big_f = False

no_f = False

for i, h in enumerate(h_list[:-1]):
    left = h_list[i]
    right = h_list[i+1]
    if left < right:
        big_f = False
        continue
    elif left == right:
        continue
    elif left - right == 1:
        if big_f:
            no_f = True
            break
        else:
            big_f = True
    elif left - right >= 2:
        no_f = True
        break

if no_f:
    print('No')
else:
    print('Yes')
>>>>>>> 15eaaa87d943dde655a49b893fcbe0c35cb496d4
