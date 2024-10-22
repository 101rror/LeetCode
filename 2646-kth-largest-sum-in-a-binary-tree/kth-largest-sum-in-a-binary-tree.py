# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        que, res = deque([root]), []

        while que:
            n = len(que)
            count = 0

            for _ in range(n):
                node = que.popleft()

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

                count += node.val
                
            res.append(count)

        return sorted(res)[-k] if k <= len(res) else -1