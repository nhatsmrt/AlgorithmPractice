public class UnionFind {
    private TreeNode root;
    private Map<Integer, TreeNode> nodeMap;

    public UnionFind() {
        nodeMap = new HashMap<Integer, TreeNode>();
        root = new TreeNode();
    }

    public int numSubsets() {
        return root.children.size();
    }

    public void add(int n) {
        TreeNode node = new TreeNode();
        node.par = root;
        root.children.add(node);
        nodeMap.put(n, node);
    }

    public void union(int a, int b) {
        if (nodeMap.containsKey(b)) {
            TreeNode first = nodeMap.get(a);
            TreeNode second = nodeMap.get(b);

            first.par.children.remove(first);
            first.par = second;
            second.children.add(first);
        }
    }

    public int findLargestSubsetSize() {
        int ret = 0;

        for (TreeNode node : root.children) {
            int candidate = node.numDescendants();
            if (candidate > ret)
                ret = candidate;
        }

        return ret;
    }

    private class TreeNode {
        public TreeNode par;
        public Set<TreeNode> children;

        public TreeNode() {
            children = new HashSet<TreeNode>();
        }

        public int numDescendants() {
            int ret = 1;

            for (TreeNode child : children)
                ret += child.numDescendants();

            return ret;
        }
    }
}



class Solution {
    public int longestConsecutive(int[] nums) {
        UnionFind sets = new UnionFind();

        for (int num : nums)
            sets.add(num);

        for (int num : nums)
            sets.union(num, num - 1);

        return sets.findLargestSubsetSize();
    }
}
