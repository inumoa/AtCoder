n = int(input())
a_list = list(map(int, input().split()))

count = 0
flag = False
hit_flag = False

for a in a_list:
    if a == count + 1:
        count += 1
        flag = True

if not flag:
    print(-1)
else:
    print(n - count)