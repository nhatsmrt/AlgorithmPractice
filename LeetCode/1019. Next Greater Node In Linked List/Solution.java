/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> data = new ArrayList<Integer>();
        ListNode it = head;
        while (it != null) {
            data.add(it.val);
            it = it.next;
        }

        if (data.size() == 0)
            return new int[0];

        Stack<Integer> mono = new Stack<Integer>();
        for (int i = data.size() - 1; i >= 0; i--) {
            int num = data.get(i);
            while (!mono.isEmpty() && mono.peek() <= num)
                mono.pop();
            if (mono.isEmpty())
                data.set(i, 0);
            else
                data.set(i, mono.peek());

            mono.push(num);
        }

        int[] ret = new int[data.size()];
        for (int i = 0; i < data.size(); i++)
            ret[i] = data.get(i);

        return ret;
    }

}
