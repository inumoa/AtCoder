N, M, L = map(int, input().split())
ABC_list = [map(int, input().split()) for _ in range(M)]
Q = int(input())
st_list = [map(int, input().split()) for _ in range(Q)]

load_list = [[[10**9+1, []] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            load_list[i][j] = [0, [i]]

for a, b, c in ABC_list:
    load_list[a-1][b-1] = c
    load_list[b-1][a-1] = c

print(load_list)

# 最短経路を求める
for i in range(N):
    for j in range(N):
        for k in range(N):
            load_list[j][k] = min(
                load_list[j][k],
                load_list[j][i]+load_list[i][k]
            )
            if load_list[j][k][0] > load_list[j][i][0] + load_list[i][k][0]:
                load_list[j][k][0] =

for content in load_list:
    print(content)

fuel_list = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        fuel_list[i][j] = load_list[i][j] // L

print(fuel_list)

for i in range(N):
    for j in range(N):
        for k in range(N):
            fuel_list[j][k] = min(
                fuel_list[j][k],
                fuel_list[j][i] + fuel_list[j][i]
            )

for s, t in st_list:
    print(fuel_list[s-1][t-1])
