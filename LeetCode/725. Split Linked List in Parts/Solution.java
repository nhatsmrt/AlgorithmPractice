/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode[] splitListToParts(ListNode root, int k) {
        int len = length(root);
        ListNode[] ret = new ListNode[k];
        if (len == 0) {
            for (int i = 0; i < k; i++)
                ret[i] = null;
            return ret;
        }

        if (len % k == 0) {
            int lengthEachPart = len / k;
            for (int i = 0; i < k; i++) {
                ListNode end = root;
                for (int j = 0; j < lengthEachPart - 1; j++) {
                    end = end.next;
                }
                ret[i] = root;
                root = end.next;
                end.next = null;
            }
        }
        else {
            int lengthShorter = len / k;
            int lengthLonger = lengthShorter + 1;
            int numPartLonger = len - lengthShorter * k;
            int numPartShorter = k - numPartLonger;

            for (int i = 0; i < numPartLonger; i++) {
                ListNode end = root;
                for (int j = 0; j < lengthLonger - 1; j++) {
                    end = end.next;
                }
                ret[i] = root;
                root = end.next;
                end.next = null;
            }

            for (int i = 0; i < numPartShorter; i++) {
                if (lengthShorter == 0)
                    ret[numPartLonger + i] = null;
                else {
                    ListNode end = root;
                    for (int j = 0; j < lengthShorter - 1; j++) {
                        end = end.next;
                    }
                    ret[numPartLonger + i] = root;
                    root = end.next;
                    end.next = null;
                }
            }
        }

        return ret;
    }

    private int length(ListNode node) {
        if (node == null)
            return 0;
        return 1 + length(node.next);
    }
}
