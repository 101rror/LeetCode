class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        d = [0] * n
        q = [i for i in range(n)]

        def get(q, i) -> int:
            if i != q[i]:
                q[i] = get(q, q[i])
            return q[i]

        for i in range(n):
            if leftChild[i] >= 0:
                q[get(q, leftChild[i])] = get(q, i)
                d[leftChild[i]] += 1
            if rightChild[i] >= 0:
                q[get(q, rightChild[i])] = get(q, i)
                d[rightChild[i]] += 1

        return d.count(0) == 1 and d.count(1) == n - 1 and len(set([get(q, i) for i in range(n)])) == 1