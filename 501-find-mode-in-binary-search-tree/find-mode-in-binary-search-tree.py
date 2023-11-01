# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        st = defaultdict(int)

        def dfs(root):
            st[root.val] += 1

            if(root.left):
                dfs(root.left)
            if(root.right):
                dfs(root.right)

        dfs(root)

        mx = max(st.values())
        
        ans = [i for i in st  if st[i] == mx]

        return ans
