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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null)
            return new ArrayList<List<Integer>>();

        Deque<TreeNode> traverseQueue = new ArrayDeque<TreeNode>();
        LinkedHashMap<TreeNode, Integer> levelMap = new LinkedHashMap<TreeNode, Integer>();

        traverseQueue.addLast(root);
        levelMap.put(root, 0);
        while(!traverseQueue.isEmpty()) {
            TreeNode node = traverseQueue.pop();
            Integer level = levelMap.get(node);

            if (node.left != null) {
                traverseQueue.addLast(node.left);
                levelMap.put(node.left, level + 1);
            }
            if (node.right != null) {
                traverseQueue.addLast(node.right);
                levelMap.put(node.right, level + 1);
            }
        }

        Integer currLevel = new Integer(0);
        ArrayList<List<Integer>> levelLists = new ArrayList<List<Integer>>();
        ArrayList<Integer> levelList = new ArrayList<Integer>();

        for (TreeNode node : levelMap.keySet()) {
            if (levelMap.get(node).equals(currLevel))
                levelList.add(node.val);
            else {
                currLevel = levelMap.get(node);
                levelLists.add(levelList);
                levelList = new ArrayList<Integer>();
                levelList.add(node.val);
            }
        }
        // Add the final level list
        levelLists.add(levelList);

        return levelLists;
    }
}
