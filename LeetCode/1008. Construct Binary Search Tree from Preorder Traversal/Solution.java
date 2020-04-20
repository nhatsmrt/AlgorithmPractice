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
    public TreeNode bstFromPreorder(int[] preorder) {
        // Time and Space Complexity: O(N)

        if (preorder.length == 0)
            return null;

        int INF = 100000000;
        TreeNode ret = new TreeNode(preorder[0]);
        bstFromPreorder(ret, -INF, INF, preorder, 1);

        return ret;
    }

    private int bstFromPreorder(TreeNode par, int lower, int upper, int[] preorder, int i) {
        if (i >= preorder.length || preorder[i] > upper || preorder[i] < lower)
            return i;

        if (preorder[i] < par.val) {
            // go to par's left subtree
            par.left = new TreeNode(preorder[i]);
            i += 1;
            i = bstFromPreorder(par.left, lower, par.val, preorder, i);
        }

        if (i < preorder.length && preorder[i] < upper && preorder[i] > par.val) {
            par.right = new TreeNode(preorder[i]);
            i += 1;
            i = bstFromPreorder(par.right, par.val, upper, preorder, i);
        }

        return i;

    }
}
