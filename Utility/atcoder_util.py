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

# 素因数分解
def prime_factorize(n):
    # 1に注意
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# ユニオンファインド木
class UnionFind:  # O(α(N))
    def __init__(self, size):  # construct a Union-Find tree (1-idx)
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):  # find the group (root) of a vertex
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_same(self, x, y):  # check two vertices are in the same group
        return self.find(x) == self.find(y)

    def unite(self, x, y):  # unite two groups
        x, y = self.find(x), self.find(y)
        if x == y:  # the same group
            return
        # unite a small one to a bigger one to balance trees
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1