/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {

        // edge case
        if (head == null || head.next == null)
            return head;

        if (head.next.next == null) {
            if (head.val >= x && head.next.val < x) {
                int tmpVal = head.val;
                head.val = head.next.val;
                head.next.val = tmpVal;
                return head;
            }
            else
                return head;
        }

        ListNode firstRear = new ListNode(-1);
        firstRear.next = head;
        while (firstRear.next != null && firstRear.next.val >= x)
            firstRear = firstRear.next;

        if (firstRear.next == null)
            return head;

        ListNode tmp = null;
        if (firstRear.next != head) {
            tmp = firstRear.next;
            firstRear.next = firstRear.next.next;
            tmp.next = head;
            head = tmp;
        }
        firstRear = new ListNode(-1);
        firstRear.next = head;

        while (firstRear.next != null && firstRear.next.val < x)
            firstRear = firstRear.next;

        if (firstRear.next == null)
            return head;

        firstRear = firstRear;
        ListNode it = firstRear;

        while(it != null && it.next != null) {
            while (it.next != null && it.next.val < x) {
                tmp = it.next;
                it.next = it.next.next;
                tmp.next = firstRear.next;
                firstRear.next = tmp;
                firstRear = firstRear.next;
            }

            it = it.next;
        }

        return head;

    }
}
