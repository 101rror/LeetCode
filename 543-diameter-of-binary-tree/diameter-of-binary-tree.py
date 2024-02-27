# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            nonlocal diameter
            if not node:
                return 0
            
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        diameter = 0
        depth(root)

        return diameter