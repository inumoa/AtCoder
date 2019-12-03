N, Q = map(int, input().split())
S = input()
lr_list = [map(int, input().split()) for _ in range(Q)]

sum_list = [0]

for i in range(N):
    if S[i] == 'C' and S[i-1] == 'A' and i:
        sum_list.append(sum_list[-1]+1)
    else:
        sum_list.append(sum_list[-1])

# [sum_list.append(sum_list[-1]+1) if s == 'C' and S[i-1] == 'A' else sum_list.append(sum_list[-1]) for i, s in enumerate(S)]

for l, r in lr_list:
    print(sum_list[r] - sum_list[l])