/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null)
            return head;

        if (head.next.next == null) {
            ListNode newHead = head.next;
            head.next = null;
            newHead.next = head;
            return newHead;

        }

        ListNode root = new ListNode(0);
        root.next = head;
        ListNode it = root;
        ListNode tmp = new ListNode(0);
        do {
            tmp = it.next;
            it.next = it.next.next;
            tmp.next = it.next.next;
            it.next.next = tmp;

            it = it.next.next;
        } while (it != null && it.next != null && it.next.next != null);

        return root.next;
    }
}
