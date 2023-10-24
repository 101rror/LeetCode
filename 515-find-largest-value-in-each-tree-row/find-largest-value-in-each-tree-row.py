# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root])

        if not root:
            return []

        while q:
            l = []
            for i in range(len(q)):
                n = q .popleft()
                l.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            ans.append(max(l))

        return ans 
        