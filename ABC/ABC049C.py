# coding:utf-8

s = input()
word_list = ['dreamer', 'eraser', 'dream', 'erase']
count = len(s)
while True:
    # 対象ありフラグ
    f = False
    # 後ろから見ていって単語列と一致するか
    for word in word_list:
        if word == s[count - len(word) : count]:
            count -= len(word)
            f = True
            break
    if not count or not f:
        break
if count:
    print('NO')
else:
    print('YES')