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
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        List<Integer> tree1 = new ArrayList<Integer>();
        inorder(root1, tree1);

        List<Integer> tree2 = new ArrayList<Integer>();
        inorder(root2, tree2);

        Set<Integer> set1 = new HashSet<Integer>(tree1);
        for (Integer num : tree2) {
            if (set1.contains(target - num))
                return true;
        }

        return false;
    }

    public void inorder(TreeNode node, List<Integer> list) {
        if (node != null) {
            inorder(node.left, list);
            list.add(node.val);
            inorder(node.right, list);
        }
    }
}
