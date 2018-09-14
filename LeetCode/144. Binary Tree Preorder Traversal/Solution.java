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
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null)
            return new ArrayList<Integer>();

        List<Integer> leftChildList = preorderTraversal(root.left);
        List<Integer> rightChildList = preorderTraversal(root.right);

        List<Integer> ret = new ArrayList<Integer>();
        ret.add(root.val);
        ret.addAll(leftChildList);
        ret.addAll(rightChildList);
        return ret;
    }
}
