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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // Time and Space Complexity: O(n)

        TreeNode root = new TreeNode(nums[0]);
        TreeNode active = root;
        TreeNode[] ancestry = new TreeNode[nums.length];
        ancestry[0] = active;
        int ptr = 0;

        for (int i = 1; i < nums.length; i++) {
            TreeNode newNode = new TreeNode(nums[i]);
            if (nums[i - 1] > nums[i])
                active.right = newNode;
            else {
                boolean isRoot = true;
                ptr -= 1;

                while (ptr != -1 && isRoot) {
                    TreeNode candidate = ancestry[ptr];
                    if (candidate.val > newNode.val) {
                        TreeNode rightChild = candidate.right;
                        candidate.right = newNode;
                        newNode.left = rightChild;

                        isRoot = false;
                    }
                    else
                        ptr -= 1;
                }

                if (isRoot) {
                    newNode.left = root;
                    root = newNode;
                }
            }

            active = newNode;
            ptr += 1;
            ancestry[ptr] = active;
        }

        return root;
    }
}
