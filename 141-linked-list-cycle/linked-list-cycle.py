# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        hasht = set()
        node = head

        while node:
            if node in hasht:
                return True
            hasht.add(node)
            node = node.next

        return False