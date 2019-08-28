_ = input()
a_list = list(map(int, input().split()))
bunshi = 1
for a in a_list:
    bunshi *= a
bunbo = sum(map(lambda x: bunshi / x, a_list))
print(bunshi/bunbo)
