# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxsum = 0

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None

        while curr:
            cur = curr.next
            curr.next = prev
            prev = curr
            curr = cur

        while prev:
            pairsum = prev.val + head.val
            maxsum = max(maxsum, pairsum)
            prev = prev.next
            head = head.next

        return maxsum