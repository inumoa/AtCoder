N, K, M = map(int, input().split())
a_list = list(map(int, input().split()))

value = (M * N) - sum(a_list)

if value <= K:
    print(max(0, value))
else:
    print(-1)