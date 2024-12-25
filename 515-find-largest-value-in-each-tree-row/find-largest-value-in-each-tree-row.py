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
            return ans

        while q:
            check = []
            for i in range(len(q)):
                n = q.popleft()
                check.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            ans.append(max(check))

        return ans
