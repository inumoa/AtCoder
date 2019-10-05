import math
import datetime
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
a, b = map(int, input().split())
prim_list = []
start = datetime.datetime.now()
# 素数のリスト作成
for i in range(0, min(a,b)//2, 2):
    if is_prime(i):
        prim_list.append(i)
print(datetime.datetime.now()-start)
print(prim_list)
