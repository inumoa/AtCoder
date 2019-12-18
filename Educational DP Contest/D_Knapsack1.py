
# # 入力
# num, weight_limit = map(int, input().split())
# wv_list = [list(map(int, input().split())) for _ in range(num)]
#
# # dpの初期化
# dp = [[0 for _ in range(num+1)] for _ in range(weight_limit+1)]
#
# for w in range(1, weight_limit+1):
#
#     for n in range(1, num+1):
#
#         weight = wv_list[n-1][0]
#         value = wv_list[n-1][1]
#
#         if weight <= w:
#             dp[w][n] = max(dp[w - weight][n-1] + value, dp[w][n-1])
#
#         else:
#             dp[w][n] = dp[w][n-1]
#
#     # print(dp[w])
#
# print(dp[-1][-1])



import numpy as np

# 入力
num, weight_limit = map(int, input().split())
wv_list = [list(map(int, input().split())) for _ in range(num)]

# dpの初期化
dp = np.zeros(weight_limit + 1)

for n in range(num):
    w = wv_list[n][0]
    v = wv_list[n][1]
    dp[w:] = np.maximum(dp[:-w] + v, dp[w:])

print(int(dp[-1]))



# from sys import stdin
# import numpy as np
#
# ds_in = lambda: list(map(int, stdin.readline().split()))  # List = ds_in()
#
# N, W = ds_in()
#
# start_time = datetime.now()
#
# values = np.zeros(W + 1, dtype=int)  # 重さi以下の最大価値
# for _ in range(N):
#     pre = values.copy()
#     wv = ds_in()  # [weight, value]
#     values[wv[0]:] = np.maximum(values[:-wv[0]] + wv[1], values[wv[0]:])
#
# print(values[-1])
#
# print(datetime.now() - start_time)



# import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools
#
#
# def LI(): return [int(x) for x in sys.stdin.readline().split()]
#
#
# def main():
#     n, w = LI()
#     aa = sorted([LI() for _ in range(n)])
#     r = [0] * (w + 1)
#     mx = 0
#     for a, b in aa:
#         mx += a
#         for i in range(min(mx, w - a), -1, -1):
#             if r[i + a] < b + r[i]:
#                 r[i + a] = b + r[i]
#
#             print(r)
#
#     return max(r)
#
#
# print(main())