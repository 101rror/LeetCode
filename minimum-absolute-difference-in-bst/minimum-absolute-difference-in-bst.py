# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []

        def fetch(root):
            nonlocal ans

            if (root==None):
                return
            if (root.left != None): 
                fetch(root.left)
            ans.append(root.val)

            if (root.right != None): 
                fetch(root.right)
        fetch(root)

        return min([(y - x) for (x, y) in pairwise(ans)])