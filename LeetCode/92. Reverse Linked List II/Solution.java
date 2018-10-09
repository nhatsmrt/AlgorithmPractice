/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private void swapNode(ListNode firstNode, ListNode secondNode) {
        int tmp = firstNode.val;
        firstNode.val = secondNode.val;
        secondNode.val = tmp;
    }

    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m >= n)
            return head;

        ListNode it1 = head;
        ListNode it2 = head;

        for (int i = 0; i < m - 1; i++)
            it1 = it1.next;

        for (int i = 0; i < n - 1; i++)
            it2 = it2.next;

        swapNode(it1, it2);
        return reverseBetween(head, m + 1, n - 1);

    }
}
