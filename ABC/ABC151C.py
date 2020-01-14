N, M = map(int, input().split())
ps_list = [input().split() for _ in range(M)]

ac_list = [False] * (N+1)
count_list = [[0, 0] for _ in range(N+1)]

for p, s in ps_list:
    p = int(p)
    if ac_list[p]:
        continue
    if s == 'AC':
        ac_list[p] = True
        count_list[p][0] += 1
    else:
        count_list[p][1] += 1

ac_count = 0
wa_count = 0

for count in count_list:
    if count[0]:
        ac_count += 1
        wa_count += count[1]

print(str(ac_count) + ' ' + str(wa_count))