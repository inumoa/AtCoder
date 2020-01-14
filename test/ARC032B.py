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


N, M = map(int, input().split())
ab_list = [map(int, input().split()) for _ in range(M)]

uf = UnionFind(N)

for a, b in ab_list:
    uf.unite(a-1, b-1)

count = 0

for i in range(N):
    if not i:
        continue
    if not uf.is_same(0, i):
        count += 1
        uf.unite(0, i)

print(count)
