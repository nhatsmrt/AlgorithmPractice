/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    // Complexity: nl + nl + nl ... (log 2 n terms) => O(nlogn * l)
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
            return null;

        if (lists.length == 1)
            return lists[0];

        while (lists.length > 1)
            lists = merge2ConsecutiveLists(lists);

        return lists[0];
    }

    // Complexity: O(nl)
    private ListNode[] merge2ConsecutiveLists(ListNode[] lists) {
        int size = lists.length;
        if (size == 1)
            return lists;

        int newSize = (size + 1) / 2;
        ListNode[] results = new ListNode[newSize];
        for (int i = 0; i < lists.length - 1; i += 2) {
            results[i / 2] = merge2Lists(lists[i], lists[i + 1]);
        }

        if (lists.length % 2 == 1)
            results[newSize - 1] = lists[lists.length - 1];

        return results;
    }

    // merge 2 sorted lists.
    // complexity: O(l)
    private ListNode merge2Lists(ListNode first, ListNode second) {
        ListNode root = new ListNode(-1);
        ListNode pt = root;
        while (first != null || second != null) {
            if (first == null) {
                pt.next = second;
                break;
            }
            else if (second == null) {
                pt.next = first;
                break;
            }

            if (first.val < second.val) {
                pt.next = first;
                first = first.next;
            }
            else {
                pt.next = second;
                second = second.next;
            }

            pt = pt.next;
        }

        return root.next;
    }
}
