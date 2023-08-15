# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(curr):
            if not curr:
                return 0

            carry_passed_back = rev(curr.next)
            new_val =  (curr.val*2 + carry_passed_back )
            curr.val = new_val% 10

            return 1 if new_val >=10 else 0
                
        carry = rev(head)
        if carry:
            head.val%=10
            head = ListNode(1,head)

        return head




            

            


