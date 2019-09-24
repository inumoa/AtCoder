n = input()
v_list = sorted(list(map(int, input().split())), reverse=True)
result = 0
for i, v in enumerate(v_list):
    if i + 1 == len(v_list):
        result += v / (2**i)
    else:
        result += v / (2**(i+1))
print(result)
