/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode findPenutlimate(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode nodePt = head;
        while (nodePt.next.next != null)
            nodePt = nodePt.next;

        return nodePt;
    }
    public void reorderList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null)
            return;

        ListNode penultimate = findPenutlimate(head);
        ListNode rear = penultimate.next;
        ListNode first = head.next;
        head.next = rear;
        rear.next = first;
        penultimate.next = null;

        reorderList(first);
    }
}
