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
    private int rightMost;
    private int leftMost;
    private Map<TreeNode, Integer> posMap;

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        if (root == null)
            return ret;

        List<List<TreeNode>> retNode = new ArrayList<List<TreeNode>>();
        leftMost = rightMost = 0;
        posMap = new HashMap<TreeNode, Integer>();
        explore(root, 0, 0);
        for (int pos = leftMost; pos <= rightMost; pos++)
            retNode.add(new ArrayList<TreeNode>());

        verticalTraverse(root, retNode, 0);
        NodeComparator comparator = new NodeComparator();
        for (List<TreeNode> nodes : retNode) {
            Collections.sort(nodes, comparator);
            List<Integer> vals = new ArrayList<Integer>();
            for (TreeNode node : nodes)
                vals.add(node.val);
            ret.add(vals);
        }

        return ret;
    }

    private void verticalTraverse(TreeNode node, List<List<TreeNode>> ret, int pos) {
        if (node != null) {
            ret.get(pos - leftMost).add(node);
            verticalTraverse(node.left, ret, pos - 1);
            verticalTraverse(node.right, ret, pos + 1);
        }
    }

    private void explore(TreeNode node, int xPos, int yPos) {
        if (node != null) {
            if (xPos > rightMost)
                rightMost = xPos;
            if (xPos < leftMost)
                leftMost = xPos;
            posMap.put(node, yPos);

            explore(node.left, xPos - 1, yPos - 1);
            explore(node.right, xPos + 1, yPos - 1);
        }
    }

    private class NodeComparator implements Comparator<TreeNode> {
        public int compare(TreeNode node1, TreeNode node2) {
            int yCoord1 = posMap.get(node1);
            int yCoord2 = posMap.get(node2);

            if (yCoord1 != yCoord2)
                return -Integer.compare(yCoord1, yCoord2);

            return Integer.compare(node1.val, node2.val);
        }
    }
}
