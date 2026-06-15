# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        dq = deque()
        cur = head

        while cur:
            dq.append(cur)
            cur = cur.next

        total = len(dq)
        mid = total // 2

        pre = dq[mid - 1]
        rem = dq[mid]

        pre.next = rem.next

        return head
