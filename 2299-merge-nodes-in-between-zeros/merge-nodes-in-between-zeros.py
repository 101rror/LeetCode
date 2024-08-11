# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        sum = 0

        while head:
            sum += head.val
            if head.val == 0 and sum:
                stack.append(sum)
                sum = 0
            head = head.next

        prev = None

        while stack:
            head = ListNode(stack.pop())
            head.next = prev
            prev = head
            
        return head