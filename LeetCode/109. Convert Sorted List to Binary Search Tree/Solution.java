/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        int size = size(head);
        return sortedListToBST(head, size);

    }

    private TreeNode sortedListToBST(ListNode head, int size) {
        if (size == 0)
            return null;
        if (size == 1)
            return new TreeNode(head.val);

        ListNode it = head;
        int leftSize = 1;
        for (int i = 0; i < size / 2 - 1; i++) {
            leftSize += 1;
            it = it.next;
        }

        ListNode mid = it.next;
        it.next = null;
        ListNode rightHalf = mid.next;
        mid.next = null;

        TreeNode ret = new TreeNode(mid.val);
        ret.left = sortedListToBST(head, leftSize);
        ret.right = sortedListToBST(rightHalf, size - leftSize - 1);

        return ret;

    }

    private int size(ListNode head) {
        int ret = 0;
        ListNode cur = head;
        while (cur != null) {
            cur = cur.next;
            ret += 1;
        }
        return ret;
    }
}
