N, K = map(int, input().split())
RSP_list = list(map(int, input().split()))
T = input()

hand_dic = {'r':0, 's':1, 'p':2}
win_hand_dic = {'r':3, 's':0, 'p':1}

dp = [[0 for _ in range(len(T))] for _ in range(3)]

for i, hand in enumerate(T[:K]):
    dp[i][hand_dic[hand]] = RSP_list[hand_dic[hand]]

print(dp)
exit()

# for i, hand in enumerate(T):
#     for num in dp[i]:
