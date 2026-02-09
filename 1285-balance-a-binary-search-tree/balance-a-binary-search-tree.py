# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return []

            left, right, val = node.left, node.right, node.val
            return dfs(left) + [val] + dfs(right)

        ans = dfs(root)
        n = len(ans) - 1

        def build(left, right):
            while left <= right:
                mid = (left + right) // 2
                root = TreeNode(ans[mid])
                root.left, root.right = build(left, mid - 1), build(mid + 1, right)
                return root

        return build(0, n)
