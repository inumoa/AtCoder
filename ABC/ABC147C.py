N = int(input())
xy_list = []
for _ in range(N):
    xy_list.append([-1 for _ in range(N)])
    for _ in range(int(input())):
        x, y = map(int, input().split())
        xy_list[-1][x-1] = y

print(xy_list)
max_val = 0
for i in range(N):
    temp_val = 0
    break_f = False
    print(f'{i}')
    for j in range(N):
        print(f'------{j}')

        if i == j:
            continue
        if xy_list[i][j] != 1:
            continue
        if xy_list[j][i] == 0:
            break_f = True
            break

        ok_f = True
        for k in range(N):
            if k == i or k == j:
                continue
            if [xy_list[i][k], xy_list[j][k]] in [[0, 1], [1, 0]]:
                ok_f = False
                break
        if ok_f:
            temp_val += 1
        else:
            break
        print(f'-------------------{temp_val}')
    if not break_f:
        max_val = max(max_val, temp_val+1)

print(max_val)