/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // remove duplicates at the beginning
        while (head != null && head.next != null && head.val == head.next.val) {
            int duplicateVal = head.val;
            while (head != null && head.val == duplicateVal)
                head = head.next;
        }

        if (head == null || head.next == null || head.next.next == null)
            return head;

        head.next = deleteDuplicates(head.next);
        return head;
    }
}
