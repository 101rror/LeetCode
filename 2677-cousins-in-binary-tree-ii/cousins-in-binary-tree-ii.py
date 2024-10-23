# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        pq = deque()
        pq.append((root.val, root))
        
        while pq:
            n = len(pq)
            levelSum = 0

            for localSum, node in pq:
                levelSum += node.val
                
            for i in range(n):
                localSum, node = pq.popleft()
                
                childSum = 0

                if node.left:
                    childSum += node.left.val
                if node.right:
                    childSum += node.right.val
                
                if node.left:
                    pq.append((childSum, node.left))
                if node.right:
                    pq.append((childSum, node.right))
                   
                node.val = levelSum - localSum
                 
        return root