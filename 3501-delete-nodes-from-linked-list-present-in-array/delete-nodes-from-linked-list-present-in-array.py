# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        t = dummy
        s = set(nums)

        while head:
            if head.val not in s:
                t.next = head
                t = t.next
            head = head.next

        t.next = None

        return dummy.next
