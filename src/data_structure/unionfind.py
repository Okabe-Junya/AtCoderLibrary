class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        """Find the root of x"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """Unite the trees of x and y"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:  # let x be the smaller tree
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """Return the size of the tree of x"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """Return True if x and y belong to the same tree"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """Return the members of the tree of x"""
        root = self.find(x)
        return [i for i in range(len(self.parents)) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
