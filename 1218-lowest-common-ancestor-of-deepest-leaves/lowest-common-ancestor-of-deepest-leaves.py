# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return (0, None)

            left, l_lca = helper(node.left)
            right, r_lca = helper(node.right)

            if left == right:
                return (left + 1, node)
            elif left > right:
                return (left + 1, l_lca)
            else:
                return (right + 1, r_lca)

        return helper(root)[1]
