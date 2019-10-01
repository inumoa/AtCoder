n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
point = 0
temp = -1
for a in a_list:
    point += b_list[a-1]
    if a - temp == 1:
        point += c_list[a-1-1]
    temp = a
print(point)