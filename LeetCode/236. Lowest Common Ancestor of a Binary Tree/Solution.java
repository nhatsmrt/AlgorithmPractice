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
    public ArrayList<TreeNode> findPath(TreeNode root, TreeNode target) {
        ArrayList<TreeNode> ret = new ArrayList<TreeNode>();
        if (root == target) {
            ret.add(root);
            return ret;
        }
        else if (root == null) {
            return ret;
        }

        ret.add(root);
        ArrayList<TreeNode> leftPath = findPath(root.left, target);
        if (leftPath.size() > 0 && leftPath.get(leftPath.size() - 1).equals(target)) {
            ret.addAll(leftPath);
            return ret;
        }

        ArrayList<TreeNode> rightPath = findPath(root.right, target);
        ret.addAll(rightPath);
        return ret;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        ArrayList<TreeNode> path1 = findPath(root, p);
        ArrayList<TreeNode> path2 = findPath(root, q);


        int path1Len = path1.size();
        int path2Len = path2.size();
        int minLen = path1Len < path2Len ? path1Len : path2Len;
        int ind = 0;

        boolean found = false;
        for (int i = 1; i < minLen; i++) {
            if (!found && path1.get(i).equals(path2.get(i))) {
                found = true;
            }

            if (found && !path1.get(i).equals(path2.get(i))) {
                ind = i - 1;
                break;
            }

            if (found && i == minLen - 1)
                ind = minLen - 1;

        }

        if (!found)
            return root;
        else
            return path1.get(ind);

    }
}
