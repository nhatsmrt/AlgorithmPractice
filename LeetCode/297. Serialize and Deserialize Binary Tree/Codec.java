/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder ret = new StringBuilder();
        serialize(root, ret);
        return ret.toString();
    }

    private void serialize(TreeNode root, StringBuilder ret) {
        if (root == null)
            return;

        int type = 0;
        if (root.left != null)
            type += 1;
        if (root.right != null)
            type += 2;

        ret.append(root.val);
        ret.append(" ");
        ret.append(type);

        if (type == 1 || type == 3) {
            ret.append(" ");
            serialize(root.left, ret);
        }

        if (type == 2 || type == 3) {
            ret.append(" ");
            serialize(root.right, ret);
        }
    }


    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty())
            return null;

        return deserialize(new Scanner(data));
    }

    private TreeNode deserialize(Scanner input) {

        int val = input.nextInt();
        int type = input.nextInt();

        TreeNode ret = new TreeNode(val);
        if (type == 1 || type == 3)
            ret.left = deserialize(input);

        if (type == 2 || type == 3)
            ret.right = deserialize(input);

        return ret;
    }

}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
