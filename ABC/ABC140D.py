n, k = map(int, input().split())
s = input()
# LR と RL，RL と LRのペアを見つけてひっくり返す
for _ in range(k):
    lr_f = 0
    rl_f = 0
    temp = None
    target_point = [0, 0]
    pair_f = False
    for i, content in enumerate(s):
        if [temp, content] == ['L', 'R']:
            if rl_f and not rl_f == i-1:
                target_point = [rl_f, i-1]
                pair_f = True
                break
            elif not lr_f:
                lr_f = i
        if [temp, content] == ['R', 'L']:
            if lr_f and not lr_f == i-1:
                target_point = [lr_f, i-1]
                pair_f = True
                break
            elif not rl_f:
                rl_f = i
        temp = content
    if not pair_f:
        if lr_f and s[-1] == 'R':
            target_point = [lr_f, len(s)-1]
        elif rl_f and s[-1] == 'L':
            target_point = [rl_f, len(s)-1]
        else:
            break
    temp_s = s[:target_point[0]]
    for i in reversed(range(target_point[0], target_point[1]+1)):
        if s[i] == 'R':
            temp_s += 'L'
        elif s[i] == 'L':
            temp_s += 'R'
    temp_s += s[target_point[1]+1:]
    s = temp_s
temp = ''
point = 0
for content in s:
    if temp == content:
        point += 1
    temp = content
print(point)