# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0,head)
		pre = 0
		dic = {0: dummy}

		while head:
			pre += head.val
			dic[pre] = head
			head = head.next

		head = dummy
		pre = 0

		while head:
			pre += head.val
			head.next = dic[pre].next
			head = head.next

		return dummy.next