n = int(input())
h_list = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i, h in enumerate(h_list):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = abs(h - h_list[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(h - h_list[i-1]), dp[i-2] + abs(h - h_list[i-2]))
print(dp[-1])
