import collections

N, M, V, P = map(int, input().split())
a_list = list(map(int, input().split()))

a_count = collections.Counter(a_list)
a_count = sorted(list(a_count.items()), reverse=True)
result = 0
temp_count = 0
for i, a in enumerate(a_count):
    result += a[1]
    temp_count += a[1]
    if temp_count >= P:
        break

tail_value = a_count[i][0]
tail_num = a_count[i][1]
upper_value = tail_value * tail_num
upper_count = tail_num

for a in a_count[i+1:]:
    if upper_value - (a[0] * upper_count) <= (N-V) * M:
        result += a[1]
        upper_count += a[1]
        upper_value += a[0]*a[1]
    else:
        break

print(result)