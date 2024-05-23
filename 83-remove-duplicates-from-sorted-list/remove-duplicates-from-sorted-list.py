class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
            
        return head
        