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


N, Q = map(int, input().split())
pab_list = [list(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(N)

for p, a, b in pab_list:
    # 連結する時
    if not p:
        uf.unite(a, b)

    # 判定をする時
    else:
        print(['No', 'Yes'][uf.is_same(a, b)])