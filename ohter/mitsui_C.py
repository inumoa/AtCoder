X = int(input())

num_list = [0]*(100001 + 105)
num_list[0] = 1

for i in range(100001 + 105):
    if i == X:
        print(num_list[X])
        exit()

    for j in [100, 101, 102, 103, 104, 105]:
        if num_list[i]:
            num_list[i+j] = 1

print(0)