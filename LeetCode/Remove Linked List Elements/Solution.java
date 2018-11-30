/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        while (head != null && head.val == val)
            head = head.next;

        if (head != null) {
            ListNode par = head;

            while (par.next != null) {
                if (par.next.val == val)
                    par.next = par.next.next;
                else
                    par = par.next;
            }
        }

        return head;
    }
}
