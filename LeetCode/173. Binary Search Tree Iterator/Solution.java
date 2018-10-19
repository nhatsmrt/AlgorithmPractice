/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    private Stack<TreeNode> nodeStack;
    private TreeNode cur;

    public BSTIterator(TreeNode root) {
        nodeStack = new Stack<TreeNode>();
        TreeNode it = root;

        while (it != null) {
            nodeStack.push(it);
            it = it.left;
        }

        if (!nodeStack.isEmpty())
            cur = nodeStack.pop();
        else
            cur = null;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return cur != null;
    }

    /** @return the next smallest number */
    public int next() {
        int ret = cur.val;

        if (cur.right != null) {
            TreeNode it = cur.right;
            while (it != null) {
                nodeStack.push(it);
                it = it.left;
            }
        }

        if (!nodeStack.isEmpty())
            cur = nodeStack.pop();
        else
            cur = null;

        return ret;

    }

}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
