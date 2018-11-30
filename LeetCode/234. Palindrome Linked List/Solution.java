/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
//     // using stack:
//     public boolean isPalindrome(ListNode head) {
//         if (head == null || head.next == null)
//             return true;

//         Stack<ListNode> s = new Stack<ListNode>();
//         ListNode cur = head;

//         while (cur != null) {
//             s.push(cur);
//             cur = cur.next;
//         }

//         cur = head;
//         while (cur != null) {
//             if (s.pop().val != cur.val)
//                 return false;

//             cur = cur.next;
//         }

//         return true;
//     }

    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null)
            return true;

        ListNode hare = head;
        ListNode tortoise = head;

        while (hare != null && hare.next != null) {
            hare = hare.next.next;
            tortoise = tortoise.next;
        }

        // odd number of elements:
        if (hare != null)
            tortoise = tortoise.next;

        tortoise = reverseList(tortoise);

        ListNode cur1 = head;
        ListNode cur2 = tortoise;

        boolean ret = true;
        while (cur2 != null) {
            if (cur1.val != cur2.val)
                ret = false;

            cur1 = cur1.next;
            cur2 = cur2.next;

        }
        tortoise = reverseList(tortoise);

        return ret;
    }

    private ListNode reverseList(ListNode head) {
        if (head != null && head.next != null) {
            ListNode tmp1 = head;
            ListNode tmp2 = head.next;

            head = reverseList(head.next);
            tmp1.next = null;
            tmp2.next = tmp1;

            return head;
        }
        else
            return head;
    }

    private void print(ListNode head) {
        ListNode cur = head;
        while (cur != null) {
            System.out.println(cur.val);
            cur = cur.next;
        }
    }

}
