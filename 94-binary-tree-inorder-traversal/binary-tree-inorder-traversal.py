# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        tr = root

        if not root:
            return []

        while tr or stack:
            while tr:
                stack.append(tr)
                tr = tr.left
            tr = stack.pop()
            ans.append(tr.val)
            tr = tr.right

        return ans