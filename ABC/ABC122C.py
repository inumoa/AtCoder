N, Q = map(int, input().split())
S = input()
lr_list = [map(int, input().split()) for _ in range(Q)]

sum_list = [0]

for i in range(N):
    if S[i] == 'C' and S[i-1] == 'A' and i:
        sum_list.append(sum_list[-1]+1)
    else:
        sum_list.append(sum_list[-1])

# print(sum_list)

for l, r in lr_list:
    print(sum_list[r] - sum_list[l])
