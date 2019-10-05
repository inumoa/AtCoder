s = input()
k = int(input())

# 1種類の文字の連続の場合
if len(set(s)) == 1:
    print(len(s) * k // 2)

else:
    count_l = []
    before_mozi = ''

    for mozi in s:
        if before_mozi == mozi:
            count_l[-1] += 1
        else:
            count_l.append(1)
        before_mozi = mozi

    # 先頭と末端の文字が同じ場合
    if s[0] == s[-1]:
        result = sum([x//2 for x in count_l[1:-1]]) * k + count_l[0]//2 + count_l[-1]//2 + (count_l[0] + count_l[-1])//2 * (k-1)

    else:
        result = sum([x//2 for x in count_l]) * k

    print(result)