/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null)
            return null;

        ListNode slowPtr = head;
        ListNode fastPtr = head.next;
        ListNode flagNode = head;
        boolean found = false;

        while (slowPtr != null && fastPtr != null && fastPtr.next != null) {
            if (slowPtr == fastPtr) {
                flagNode = slowPtr;
                found = true;
                break;
            }

            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next.next;

        }

        if (!found)
            return null;

        int cnt = 1;
        ListNode nodeCnt = head;

        while(nodeCnt != flagNode) {
            cnt += 1;
            nodeCnt = nodeCnt.next;
        }

        slowPtr = head;
        fastPtr = head;
        for (int i = 0; i < cnt; i++)
            fastPtr = fastPtr.next;

        while (slowPtr != fastPtr) {
            slowPtr = slowPtr.next;
            fastPtr = fastPtr.next;
        }

        return slowPtr;
    }
}
