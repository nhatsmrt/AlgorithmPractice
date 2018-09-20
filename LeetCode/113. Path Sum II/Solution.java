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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();


        if (root == null) {
            return ret;
        }


        int remainder = sum - root.val;


        if (root.left == null && root.right == null && remainder != 0)
            return ret;



        if (remainder == 0) {
            if (root.left == null && root.right == null) {
                List<Integer> path = new ArrayList<Integer>();
                path.add(root.val);
                ret.add(path);
                return ret;
            }
        }


        List<List<Integer>> subPathLeft = pathSum(root.left, remainder);
        List<List<Integer>> subPathRight = pathSum(root.right, remainder);

        for (List<Integer> subPath : subPathLeft) {
            if (!subPath.isEmpty()) {
                subPath.add(0, root.val);
                ret.add(subPath);
            }
        }

        for (List<Integer> subPath : subPathRight) {
            if (!subPath.isEmpty()) {
                subPath.add(0, root.val);
                ret.add(subPath);
            }
        }

        return ret;

    }
}
