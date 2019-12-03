import math
import collections

# 組み合わせ数
def combination(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

N = int(input())
a_list = list(map(int, input().split()))

sum_list = [0]
for a in a_list:
    sum_list.append(sum_list[-1]+a)

sum_list = sum_list[1:]

c = collections.Counter(sum_list)

count = 0

for key in c.keys():
    if key == 0:
        count += c[0]
    if c[key] > 1:
        count += combination(c[key], 2)

print(count)