/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private ListNode root = new ListNode(-1);
    private ListNode it = root;
    private int tmp = 0;

    private ListNode mergeSort(ListNode head, int length) {
        if (length < 2)
            return head;

        if (length == 2) {
            if (head.next.val <= head.val)
                swapValue(head, head.next);

            return head;
        }

        int firstHalf = length / 2;
        int secondHalf = length - firstHalf;
        it = head;
        for (int i = 0; i < firstHalf - 1; i++)
            it = it.next;

        ListNode secondHead = it.next;
        it.next = null;

        head = mergeSort(head, firstHalf);
        secondHead = mergeSort(secondHead, secondHalf);
        head = merge(head, secondHead);

        return head;
    }

    public ListNode sortList(ListNode head) {
        head = mergeSort(head, length(head));
        return head;
    }

    private int length(ListNode head) {
        ListNode cur = head;
        int ret = 0;

        while (cur != null) {
            ret += 1;
            cur = cur.next;
        }

        return ret;
    }

    private void swapValue(ListNode a, ListNode b) {
        tmp = a.val;
        a.val = b.val;
        b.val = tmp;
    }

    // merge two sorted lists
    private ListNode merge(ListNode first, ListNode second) {
        if (first == null)
            return second;
        if (second == null)
            return first;

        it = root;
        while (first != null && second != null) {
            if (first.val < second.val) {
                it.next = first;
                first = first.next;
            }
            else {
                it.next = second;
                second = second.next;
            }
            it = it.next;
        }

        if (first != null)
            it.next = first;
        else if (second != null)
            it.next = second;

        return root.next;
    }
}
