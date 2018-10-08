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
    public TreeNode deleteNode(TreeNode root, int key) {
        root = deleteNodeHelper(root, null, key);
        return root;
    }

    private TreeNode deleteNodeHelper(TreeNode root, TreeNode par, int key) {


        if (root == null)
            return root;

        if (root.val < key) {
            deleteNodeHelper(root.right, root, key);
            return root;
        }

        if (root.val > key) {
            deleteNodeHelper(root.left, root, key);
            return root;
        }

        // if the found node is leaf:
        if (root.left == null && root.right == null) {

            if (par != null) {
                if (par.left == root)
                    par.left = null;
                else
                    par.right = null;
            }

            return null;
        }


        if (root.left == null) {
            TreeNode newRoot = root.right;

            if (par != null) {
                if (par.left == root)
                    par.left = newRoot;
                else
                    par.right = newRoot;
            }

            return newRoot;
        }

        if (root.right == null) {
            TreeNode newRoot = root.left;

            if (par != null) {
                if (par.left == root)
                    par.left = newRoot;
                else
                    par.right = newRoot;
            }

            return newRoot;
        }

        TreeNode successor = inorderSuccessor(root);
        root.val = successor.val;
        deleteNodeHelper(root.right, root, root.val);
        return root;
    }

    private TreeNode inorderSuccessor(TreeNode root) {
        if (root == null || root.right == null)
            return null;

        List<TreeNode> traverseRight = traverseInorder(root.right);
        return traverseRight.get(0);
    }

    private List<TreeNode> traverseInorder(TreeNode root) {
        List<TreeNode> ret = new ArrayList<TreeNode>();

        if (root == null)
            return ret;

        List<TreeNode> leftList = traverseInorder(root.left);
        List<TreeNode> rightList = traverseInorder(root.right);

        ret.addAll(leftList);
        ret.add(root);
        ret.addAll(rightList);
        return ret;
    }
}
