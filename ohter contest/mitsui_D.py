N = int(input())
S = input()

count = 0

memo = [[-1 for _ in range(10)] for _ in range(10)]

num_set = set(S)
# memo = [[-1 for _ in range(len(num_list))] for _ in range(len(num_list))]

for i in range(len(S) - 3 + 1):
    i_target = int(S[i])
    for j in range(i + 1, len(S) - 2 + 1):
        j_target = int(S[j])
        if memo[i_target][j_target] == -1:
            memo[i_target][j_target] = 1
            count += len(set(S[j + 1:]))

    fin_f = True

    for x_num in num_set:
        for y_num in num_set:
            if memo[int(x_num)][int(y_num)] == -1:
                fin_f = False

    if fin_f:
        break

print(count)