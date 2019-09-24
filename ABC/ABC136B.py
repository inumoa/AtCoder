# coding:utf-8

n = int(input())

keta = len(str(n))

count = 0

for i in range(keta):
    # 面倒なので0はとばす
    # 1 ~ 桁数-1まで考える
    if i == 0:
        continue
    elif i == 1:
        count += 9
    else:
        if i % 2:
            # 最上位桁は9パターン，それ以下は10パターン
            count += 10 ** (i-1) * 9

# 最上位桁のカウント
if keta % 2:
    count += n - 10 ** (keta - 1) + 1

print(count)