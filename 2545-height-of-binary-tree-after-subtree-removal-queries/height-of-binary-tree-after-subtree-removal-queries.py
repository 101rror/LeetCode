# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root, queries):
        dct = defaultdict(int)
        ans = []

        @lru_cache(None)
        def height(node):
            if not node:
                return -1

            return 1 + max(height(node.left), height(node.right))

        def dfs(node, depth, maxval):
            if not node:
                return

            dct[node.val] = maxval

            dfs(node.left, depth + 1, max(maxval, depth + 1 + height(node.right)))
            dfs(node.right, depth + 1, max(maxval, depth + 1 + height(node.left)))

        dfs(root, 0, 0)

        for i in queries:
            ans.append(dct[i])

        return ans
