class Solution:
    def sumNumbers(self, root: Optional[TreeNode] , val = 0) -> int:
        if not root:
            return 0

        q = [(root , str(root.val))]
        ans = 0

        while(q):
            node ,val = q.pop()

            if (not node.left and not node.right):
                ans += int(val)

            if node.left:
                q.append((node.left , val + str(node.left.val)))

            if node.right:
                q.append((node.right , val + str(node.right.val)))

        return ans