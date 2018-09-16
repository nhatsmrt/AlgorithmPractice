/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {

    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null)
            return head;

        ListNode slowNodeIt = head;
        ListNode fastNodeIt = head.next;
        ListNode tmp1;
        ListNode tmp2;

        while (fastNodeIt != null && fastNodeIt.next != null) {
            // put fastNodeIt.next after slowNodeIt
            tmp1 = slowNodeIt.next;
            tmp2 = fastNodeIt.next.next;
            slowNodeIt.next = fastNodeIt.next;
            slowNodeIt.next.next = tmp1;
            fastNodeIt.next = tmp2;

            fastNodeIt = fastNodeIt.next;
            slowNodeIt = slowNodeIt.next;
        }

        return head;
    }
}
