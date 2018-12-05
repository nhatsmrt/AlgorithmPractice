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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Queue<Integer> inorderQ = new LinkedList<Integer>();
        Stack<Integer> postorderS = new Stack<Integer>();

        for (int i = 0; i < postorder.length; i++) {
            inorderQ.add(inorder[i]);
            postorderS.push(postorder[i]);
        }

        return buildTree(inorderQ, postorderS);
    }

    private TreeNode buildTree(Queue<Integer> inorder, Stack<Integer> postorder) {
        if (postorder.size() == 0)
            return null;

        TreeNode ret = new TreeNode(postorder.pop());
        if (!postorder.isEmpty()) {
            int numLeftNodes = 0;

            Queue<Integer> inorderLeft = new LinkedList<Integer>();
            while (inorder.peek() != ret.val) {
                inorderLeft.add(inorder.remove());
                numLeftNodes += 1;
            }
            inorder.remove();

            Queue<Integer> tmp = new LinkedList<Integer>();
            Stack<Integer> postorderRight = new Stack<Integer>();

            while (postorder.size() > numLeftNodes)
                tmp.add(postorder.pop());
            q2s(tmp, postorderRight);
            s2q(postorderRight, tmp);
            q2s(tmp, postorderRight);

            ret.left = buildTree(inorderLeft, postorder);
            ret.right = buildTree(inorder, postorderRight);
        }

        return ret;

    }

    private void q2s(Queue<Integer> q, Stack<Integer> s) {
        while (!q.isEmpty())
            s.push(q.remove());
    }

    private void s2q(Stack<Integer> s, Queue<Integer> q) {
        while (!s.isEmpty())
            q.add(s.pop());
    }


}
