/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {


        ListNode root = new ListNode(-1);
        ListNode it = root;
        int brought = 0;
        int newVal;

        do {
            newVal = (l1.val + l2.val + brought) % 10;
            brought = (l1.val + l2.val + brought) / 10;

            it.next = new ListNode(newVal);
            it = it.next;

            l1 = l1.next;
            l2 = l2.next;
        } while(l1 != null && l2 != null);

        while(l1 != null) {
            newVal = (l1.val + brought) % 10;
            brought = (l1.val + brought) / 10;
            it.next = new ListNode(newVal);
            it = it.next;

            l1 = l1.next;
        }

        while(l2 != null) {
            newVal = (l2.val + brought) % 10;
            brought = (l2.val + brought) / 10;
            it.next = new ListNode(newVal);
            it = it.next;

            l2 = l2.next;
        }

        if (brought != 0)
            it.next = new ListNode(brought);

        return root.next;

    }
}
