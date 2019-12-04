n, k, q = map(int, input().split())
a_list = [int(input()) for _ in range(q)]
if k > q:
    for _ in range(n):
        print('Yes')
else:
    point_list = [0 for _ in range(n)]
    for a in a_list:
        point_list[a-1] += 1
    all_sum = sum(point_list)
    for point in point_list:
        if k - all_sum + point > 0:
            print('Yes')
        else:
            print('No')