_, k = map(int, input().split())
h = list(map(int, input().split()))
count = 0
for member in h:
    if member >= k:
        count += 1
print(count)