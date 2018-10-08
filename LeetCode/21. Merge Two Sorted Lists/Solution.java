/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode root = new ListNode(-1);
        ListNode pt = root;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                pt.next = l2;
                break;
            }
            else if (l2 == null) {
                pt.next = l1;
                break;
            }

            if (l1.val < l2.val) {
                pt.next = l1;
                l1 = l1.next;
            }
            else {
                pt.next = l2;
                l2 = l2.next;
            }

            pt = pt.next;
        }

        return root.next;

    }
}
