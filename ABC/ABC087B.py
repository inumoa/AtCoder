# coding:utf-8

go_hyaku = input()
hyaku = input()
go_zyu = input()
x = input()

count = 0

for i in range(int(go_hyaku) + 1):
    for j in range(int(hyaku) + 1):
        for k in range(int(go_zyu) + 1):
            if 500*i + 100*j + 50*k == int(x):
                count += 1

print(count)