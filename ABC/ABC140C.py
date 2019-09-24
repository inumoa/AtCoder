n = int(input())
b_list = list(map(int, input().split()))
temp = 10**5
max_sum = 0
for b in b_list:
    max_sum += min(b, temp)
    temp = b
print(max_sum+temp)