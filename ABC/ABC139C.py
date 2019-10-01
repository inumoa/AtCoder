<<<<<<< HEAD
n = int(input())
h_list = [int(x) for x in input().split()]
count = 0
temp_count = 0
for i, h in enumerate(h_list[:-1]):
    if h >= h_list[i+1]:
        temp_count += 1
    else:
        count = max(count, temp_count)
        temp_count = 0
if temp_count:
    count = max(count, temp_count)
=======
n = int(input())
h_list = [int(x) for x in input().split()]
count = 0
temp_count = 0
for i, h in enumerate(h_list[:-1]):
    if h >= h_list[i+1]:
        temp_count += 1
    else:
        count = max(count, temp_count)
        temp_count = 0
if temp_count:
    count = max(count, temp_count)
>>>>>>> 15eaaa87d943dde655a49b893fcbe0c35cb496d4
print(count)