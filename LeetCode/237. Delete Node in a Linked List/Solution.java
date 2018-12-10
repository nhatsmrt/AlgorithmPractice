/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        ListNode cur = node;

        if (cur.next.next != null) {
            while (cur.next.next != null) {
                cur.val = cur.next.val;
                cur = cur.next;
            }
        }

        cur.val = cur.next.val;
        cur.next = null;

    }
}
