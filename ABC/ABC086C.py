# coding:utf-8

# 入力受け付け
plan_list = [[0, 0, 0]]
for _ in range(int(input())):
    plan_list.append([int(x) for x in input().split(' ')])

# 未出力フラグ
f = True

for i in range(len(plan_list)):
    if i == len(plan_list) - 1:
        break
    else:
        time = plan_list[i+1][0] - plan_list[i][0]
        step = abs(plan_list[i+1][1] - plan_list[i][1]) + abs(plan_list[i+1][2] - plan_list[i][2])

        # 時間よりステップ数が多い，もしくはステップ数と時間の偶奇が異なる場合
        if step > time or (step%2 + time%2)%2:
            print('No')
            f = False
            break

if f:
    print('Yes')