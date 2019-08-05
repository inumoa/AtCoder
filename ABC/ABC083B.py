# coding:utf-8
n, a, b = [int(x) for x in input().split(' ')]
count = 0
result = 0

while True:
    if count > n:
        break

    # 各桁を分割してリスト化，合計する
    if b >= sum([int(x) for x in list(str(count))]) >= a:
        result += count

    count += 1

print(result)