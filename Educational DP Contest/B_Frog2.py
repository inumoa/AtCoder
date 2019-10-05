n, k = map(int, input().split())
h_list = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(k):
