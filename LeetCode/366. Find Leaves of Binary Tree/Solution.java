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
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        findLeaves(root, ret);
        return ret;
    }

    private int findLeaves(TreeNode node, List<List<Integer>> ret) {
        if (node == null)
            return -1;

        int level = Math.max(findLeaves(node.left, ret), findLeaves(node.right, ret)) + 1;
        if (ret.size() == level)
            ret.add (new ArrayList<Integer>());
        ret.get(level).add(node.val);
        return level;
    }
}
