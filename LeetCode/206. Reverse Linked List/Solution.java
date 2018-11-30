/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head != null && head.next != null) {
            ListNode tmp1 = head;
            ListNode tmp2 = head.next;

            head = reverseList(head.next);
            tmp1.next = null;
            tmp2.next = tmp1;

            return head;
        }
        else
            return head;
    }
}
