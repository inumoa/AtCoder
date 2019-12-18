value_list = [6000, -2000, -5000, 6000]
dp = [0, 0, 0, 0, 0]
for i in range(1, len(value_list)+1):
	dp[i] = max(dp[i-1], value_list[i-1])
print(dp[-1])