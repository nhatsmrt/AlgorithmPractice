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
        ListNode it = head;
        while (it != null && it.next != null) {
            if (it.val == it.next.val)
                it.next = it.next.next;
            else
                it = it.next;
        }
        return head;
    }
}
