# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if (b == 0):
                return a
            else:
                return gcd(b, a % b)

        curr = head

        while(curr and curr.next):
            newgcd = gcd(curr.val, curr.next.val) 
            newvalue = ListNode(newgcd)

            newvalue.next = curr.next
            curr.next = newvalue
            curr = curr.next.next

        return head
        