# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        last = head

        while n:
            first = first.next
            n -= 1

        if not first:
            return head.next

        while first.next:
            last = last.next
            first = first.next

        last.next = last.next.next
        return head