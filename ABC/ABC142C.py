n = int(input())
a_list = list(map(int, input().split()))
a_dict = {}
for i, a in enumerate(a_list):
    a_dict[a] = i
result_list = []
for key in sorted(list(a_dict.keys())):
    result_list.append(str(a_dict[key]+1))
print(' '.join(result_list))