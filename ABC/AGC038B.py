n, k = map(int, input().split())
p_list = list(map(int, input().split()))

count = 0
not_change_f = False

for i in range(n-k+1):
    print(p_list[i:i+k])
    if (p_list[i+k-1] - p_list[i]) >= k-1:
        if not p_list[i:i+k] == sorted(p_list[i:i+k]):
            count += 1
            print('@')
        elif not not_change_f:
            count += 1
            print('@')
            not_change_f = True
    else:
        count += 1
        print('@')

print(count)
