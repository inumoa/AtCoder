a = int(input())
b = int(input())
num_list = [1, 2, 3]
print(list(set(num_list) - set([a, b]))[0])