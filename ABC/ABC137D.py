n, m = map(int, input().split())
b_list = [[] for _ in range(m)]
for _ in range(n):
    a, b = map(int, input().split())
    if m >= a:
        b_list[a - 1].append(b)
for ab in b_list:
    ab.sort(reverse=True)
print(b_list)
result = 0
for i in reversed(range(1, m+1)):
    # print(b_list[:i])
    temp_list = []
    for b in b_list[:i]:
        if not b == []:
            temp_list.append(b[0])
        else:
            temp_list.append(-1)
    print(temp_list)
    index = temp_list.index(max(temp_list))
    if not index == -1:
        result += b_list[index].pop(0)
        if b_list[index] == []:
            b_list[index] = [-1]
print(result)