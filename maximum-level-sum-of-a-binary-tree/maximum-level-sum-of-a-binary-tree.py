class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, counts):
            if (node is not None):
                counts[level] += node.val
                dfs(node.left, level + 1, counts)
                dfs(node.right, level + 1, counts)
        
        counts = Counter()
        dfs(root, 1, counts)
        ans = counts.most_common(1)[0][0]
        
        return ans