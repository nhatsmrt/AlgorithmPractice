/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode root = new ListNode(-1);
        root.next = head;
        ListNode par = root;
        ListNode lastSorted = root;
        ListNode tmp = null;
        ListNode it = null;

        while (par != null && par.next != null) {
            tmp = par.next;
            par.next = par.next.next;

            it = root;
            while (it != lastSorted && it.next.val < tmp.val) {
                it = it.next;
            }

            tmp.next = it.next;
            it.next = tmp;

            if (lastSorted == it)
                lastSorted = lastSorted.next;

            par = lastSorted;


        }

        return root.next;
    }

    private void printList(ListNode head) {
        ListNode it = head;
        while (it != null) {
            System.out.println(it.val);
            it = it.next;
        }

        System.out.println();
    }
}
