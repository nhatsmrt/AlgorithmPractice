/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null)
            return false;

        ListNode tortoise = head;
        ListNode hare = head.next;

        while (hare != null) {
            if (tortoise == hare)
                return true;
            if (hare.next == null)
                return false;

            tortoise = tortoise.next;
            hare = hare.next.next;
        }

        return false;
    }
}
