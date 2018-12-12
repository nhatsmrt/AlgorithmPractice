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
    private Map<TreeNode, Integer> maxPathSumMap;
    private Map<TreeNode, Integer> maxPathSumFromMap;


    public int maxPathSum(TreeNode root) {
        maxPathSumMap = new HashMap<TreeNode, Integer>();
        maxPathSumFromMap = new HashMap<TreeNode, Integer>();
        return maxPathSumDP(root);
    }

    private int maxPathSumDP(TreeNode root) {
        if (root == null)
            return 0;

        if (maxPathSumMap.containsKey(root))
            return maxPathSumMap.get(root);

        int[] candidates = new int[3];
        candidates[0] = root.val;
        if (maxPathSumFrom(root.left) > 0)
            candidates[0] += maxPathSumFrom(root.left);

        if (maxPathSumFrom(root.right) > 0)
            candidates[0] += maxPathSumFrom(root.right);

        if (root.left != null)
            candidates[1] = maxPathSumDP(root.left);
        else
            candidates[1] = candidates[0];

        if (root.right != null)
            candidates[2] = maxPathSumDP(root.right);
        else
            candidates[2] = candidates[0];



        int ret = max(candidates);
        maxPathSumMap.put(root, ret);
        return ret;

    }

    private int maxPathSumFrom(TreeNode root) {
        if (root == null)
            return 0;

        if (maxPathSumFromMap.containsKey(root))
            return maxPathSumFromMap.get(root);

        int ret = root.val +
            Math.max(0, Math.max(maxPathSumFrom(root.left), maxPathSumFrom(root.right)));
        maxPathSumFromMap.put(root, ret);

        return ret;

    }

    private int max(int[] arr) {
        int cur = arr[0];

        for (int num : arr) {
            if (num > cur)
                cur = num;
        }

        return cur;
    }
}
