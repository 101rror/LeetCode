from heapq import heappush, heappop


class DisjointSet:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]

    def find(self, node: int) -> int:
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)

        self.parent[root1] = self.parent[root2] = min(root1, root2)


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        disjoint_set = DisjointSet(n)

        tree_size = 0
        res = float("inf")

        eligible = []
        for node1, node2, strength, must in edges:
            if must == 1:
                if disjoint_set.find(node1) == disjoint_set.find(node2):
                    return -1

                res = min(res, strength)
                disjoint_set.union(node1, node2)
                tree_size += 1

                continue

            heappush(eligible, (-strength, node1, node2))

        strengths = []
        while eligible and tree_size < n - 1:
            neg_str, node1, node2 = heappop(eligible)

            if disjoint_set.find(node1) == disjoint_set.find(node2):
                continue

            strength = -neg_str
            heappush(strengths, strength)
            tree_size += 1
            disjoint_set.union(node1, node2)

        if tree_size != n - 1:
            return -1

        while strengths and strengths[0] < res and k > 0:
            k -= 1
            res = min(res, heappop(strengths) * 2)

        return res if not strengths else min(res, strengths[0])