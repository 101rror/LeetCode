# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        st = set()

        for x, y, flag in descriptions:
            if x not in nodes:
                nodes[x] = TreeNode(x)
            if y not in nodes:
                nodes[y] = TreeNode(y)

            if flag:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]

            st.add(y)

        for val in nodes:
            if val not in st:
                return nodes[val]
