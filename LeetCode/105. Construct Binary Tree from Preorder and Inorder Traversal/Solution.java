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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Queue<Integer> preorderQ = new LinkedList<Integer>();
        Queue<Integer> inorderQ = new LinkedList<Integer>();

        for (int i = 0; i < preorder.length; i++) {
            preorderQ.add(preorder[i]);
            inorderQ.add(inorder[i]);
        }

        return buildTree(preorderQ, inorderQ);
    }

    private TreeNode buildTree(Queue<Integer> preorder, Queue<Integer> inorder) {
        if (preorder.size() == 0)
            return null;

        TreeNode ret = new TreeNode(preorder.remove());
        if (!preorder.isEmpty()) {
            int numLeftNodes = 0;

            Queue<Integer> inorderLeft = new LinkedList<Integer>();
            while (inorder.peek() != ret.val) {
                inorderLeft.add(inorder.remove());
                numLeftNodes += 1;
            }
            inorder.remove();

            Queue<Integer> preorderLeft = new LinkedList<Integer>();
            for (int j = 0; j < numLeftNodes; j++)
                preorderLeft.add(preorder.remove());

            ret.left = buildTree(preorderLeft, inorderLeft);
            ret.right = buildTree(preorder, inorder);
        }

        return ret;

    }
}
