/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null)
            return null;

        ListNode cur1 = headA;
        ListNode cur2 = headB;
        int size1 = size(headA);
        int size2 = size(headB);

        if (size1 < size2) {
            for (int i = 0; i < size2 - size1; i++)
                cur2 = cur2.next;
        }
        else {
            for (int i = 0; i < size1 - size2; i++)
                cur1 = cur1.next;
        }

        while (cur1 != null) {
            if (cur1 == cur2)
                return cur1;

            cur1 = cur1.next;
            cur2 = cur2.next;
        }

        return null;
    }

    private int size(ListNode head) {
        int size = 0;

        ListNode cur = head;
        while (cur != null) {
            size += 1;
            cur = cur.next;
        }

        return size;
    }
}
