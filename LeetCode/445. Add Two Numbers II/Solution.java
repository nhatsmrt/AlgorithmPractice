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
        int len1 = length(l1);
        int len2 = length(l2);
        ListNode ret = addTwoNumbers(l1, l2, len1, len2);
        if (ret.val >= 10) {
            ListNode tmp = ret;
            ret = new ListNode(1);
            tmp.val -= 10;
            ret.next = tmp;
        }

        return ret;
    }

    private ListNode addTwoNumbers(ListNode l1, ListNode l2, int len1, int len2) {
        if (len1 == len2) {
            l1.val += l2.val;

            if (l1.next != null) {
                l1.next = addTwoNumbers(l1.next, l2.next, len1 - 1, len2 - 1);
                if (l1.next.val >= 10) {
                    l1.next.val -= 10;
                    l1.val += 1;
                }
            }

            return l1;
        }
        else if (len1 < len2) {
            l2.next = addTwoNumbers(l1, l2.next, len1, len2 - 1);
            if (l2.next.val >= 10) {
                l2.next.val -= 10;
                l2.val += 1;
            }
            return l2;
        }
        else {
            l1.next = addTwoNumbers(l1.next, l2, len1 - 1, len2);
            if (l1.next.val >= 10) {
                l1.next.val -= 10;
                l1.val += 1;
            }
            return l1;
        }
    }

    private int length(ListNode l) {
        return l == null ? 0 : 1 + length(l.next);
    }
}
