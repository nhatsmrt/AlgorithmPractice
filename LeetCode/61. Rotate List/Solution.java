/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int listLength(ListNode head) {
        int len = 0;
        while (head != null) {
            len += 1;
            head = head.next;
        }

        return len;
    }

    public ListNode findRear(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode it = head;
        while(it.next != null)
            it = it.next;

        return it;
    }

    public ListNode rotateRight(ListNode head, int k) {
        // ListNode curHead = head;
        if (k == 0)
            return head;

        int len = listLength(head);
        if (len == 0 || len == 1)
            return head;

        if (k >= len)
            return rotateRight(head, k % len);


        ListNode newHeadPar = head;
        ListNode curRear = findRear(head);

        for (int i = 1; i < len - k; i++)
            newHeadPar = newHeadPar.next;


        curRear.next = head;
        head = newHeadPar.next;
        newHeadPar.next = null;

        return head;
    }
}
