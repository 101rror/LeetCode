/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ModifiedList(int[] nums, ListNode head) {
        HashSet<int> set = new(nums);
        List<ListNode> helper = new List<ListNode>();

        while (head != null) {
            if (!set.Contains(head.val)) {
                helper.Add(head);
            }
            head = head.next;
        }
        helper.Reverse();
        ListNode prev = null;

        foreach (ListNode node in helper) {
            head = new ListNode(node.val, prev);
            prev = head;
        }

        return head;
    }
}