class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head

        while curr and curr.val == stack.pop():
            curr = curr.next

        return curr is None