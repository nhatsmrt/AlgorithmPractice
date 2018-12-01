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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        return zigzagLevelOrder(root, 1);
    }

    private List<List<Integer>> zigzagLevelOrder(TreeNode root, int level) {
        if (root == null)
            return new ArrayList<List<Integer>>();

        List<List<Integer>> left = zigzagLevelOrder(root.left, level + 1);
        List<List<Integer>> right = zigzagLevelOrder(root.right, level + 1);

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> base = new ArrayList<Integer>();
        base.add(root.val);
        ret.add(base);

        int maxDepth = Math.max(left.size(), right.size());
        for (int i = 0; i < maxDepth; i++) {
            if (i >= left.size() || left.get(i).isEmpty())
                ret.add(right.get(i));
            else if (i >= right.size() || right.get(i).isEmpty())
                ret.add(left.get(i));
            else {
                if ((level + i + 1) % 2 != 0) {
                    left.get(i).addAll(right.get(i));
                    ret.add(left.get(i));
                }
                else {
                    right.get(i).addAll(left.get(i));
                    ret.add(right.get(i));
                }
            }
        }

        return ret;

    }


}
