class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

            maximum = max(leftDepth, rightDepth)

            return 1 + maximum