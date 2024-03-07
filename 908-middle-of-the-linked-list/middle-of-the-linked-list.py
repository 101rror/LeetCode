class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head

        while (middle and middle.next):
            head = head.next
            middle = middle.next.next

        return head