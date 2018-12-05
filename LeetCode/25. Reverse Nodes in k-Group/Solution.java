/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode cur = head;
        for (int i = 0; i < k - 1; i++) {
            if (cur == null)
                return head;
            else
                cur = cur.next;
        }
        if (cur == null)
            return head;

        cur.next = reverseKGroup(cur.next, k);
        ListNode tmp = cur.next;
        cur.next = null;
        cur = head;
        head = reverse(head);
        cur.next = tmp;
        return head;
    }

    private ListNode reverse(ListNode head) {
        if (head != null && head.next != null) {
            ListNode tmp = head.next;
            ListNode ret = reverse(head.next);
            tmp.next = head;
            return ret;
        }
        else
            return head;
    }
}
