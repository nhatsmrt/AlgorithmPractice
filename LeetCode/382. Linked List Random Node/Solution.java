/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    ListNode head;
    Random randomizer;

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        this.head = head;

    }

    /** Returns a random node's value. */
    public int getRandom() {
        if (head.next == null)
            return head.val;

        ListNode cur = head;
        ListNode nodeIt = head.next;
        int curNum = 2;

        while(nodeIt != null) {
            Random randomizer = new Random();
            int choice = randomizer.nextInt(curNum);

            if (choice == 0)
                cur = nodeIt;

            curNum += 1;
            nodeIt = nodeIt.next;
        }

        return cur.val;

    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
