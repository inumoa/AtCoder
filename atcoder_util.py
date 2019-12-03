import math

# 組み合わせ数
def combination(n, r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

# エラトステネスの篩
# nまでの素数のリスト
def eratosthenes(n):
    prime_list = [True]*(n+1)
    prime_list[0:2] = [False, False]
    for val in range(2, n//2+1):
        if prime_list[val]:
            for i in range(val*2, n+1, val):
                prime_list[i] = False
    return [i for i in range(n+1) if prime_list[i]]