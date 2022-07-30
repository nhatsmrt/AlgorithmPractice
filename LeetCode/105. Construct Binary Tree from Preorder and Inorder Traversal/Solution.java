/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private Map<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Time and Space Complexity: O(N)

        inorderIndex = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndex.put(inorder[i], i);
        }

        return build(preorder, inorder, 0, preorder.length - 1, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int[] inorder, int preStart, int preEnd, int inStart, int inEnd) {
        if (preStart > preEnd) {
            return null;
        }

        int rootVal = preorder[preStart];
        int inorderRootInd = inorderIndex.get(rootVal);

        int leftSize = inorderRootInd - inStart;
        int rightSize = inEnd - inorderRootInd;

        int preLeftEnd = preStart + leftSize;
        int preRightStart = preLeftEnd + 1;

        return new TreeNode(
            rootVal,
            build(preorder, inorder, preStart + 1, preLeftEnd, inStart, inorderRootInd - 1),
            build(preorder, inorder, preRightStart, preEnd, inorderRootInd + 1, inEnd)
        );
    }
}
