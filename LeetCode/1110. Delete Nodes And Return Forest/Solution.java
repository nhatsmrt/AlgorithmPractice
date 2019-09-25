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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {

        Set<Integer> toDelete = new HashSet<Integer>();
        for (int val : to_delete)
            toDelete.add(val);

        List<TreeNode> ret = new ArrayList<TreeNode>();
        delNodes(root, toDelete, ret, true);
        return ret;

    }

    private TreeNode delNodes(TreeNode node, Set<Integer> toDelete, List<TreeNode> ret, boolean isRoot) {
        if (node != null) {
            if (toDelete.contains(node.val)) {
                delNodes(node.left, toDelete, ret, true);
                delNodes(node.right, toDelete, ret, true);

                return null;
            }
            else {
                if (isRoot)
                    ret.add(node);

                node.left = delNodes(node.left, toDelete, ret, false);
                node.right = delNodes(node.right, toDelete, ret, false);
            }
        }

        return node;
    }
}
