n = int(input())
a_list = []
for _ in range(n):
    a_list.append(int(input()))
max_list = [0, 0]
for a in a_list:
    if a > max_list[0]:
        max_list[0] = a
    elif a > max_list[1]:
        max_list[1] = a
for a in a_list:
    if not a == max_list[0]:
        print(max_list[0])
    else:
        print(max_list[1])
