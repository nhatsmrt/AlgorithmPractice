class UnionFind {
    private Map<Integer, UFNode> nodesMap;
    private int numSet;

    public UnionFind(int n) {
        nodesMap = new HashMap<Integer, UFNode>();
        for (int i = 0; i < n; i++)
            nodesMap.put(i, new UFNode(i));

        numSet = n;
    }


    public int numSet() {
        return numSet;
    }


    public void union(int a, int b) {
        UFNode root1 = findRoot(nodesMap.get(a));
        UFNode root2 = findRoot(nodesMap.get(b));

        if (root1 != root2) {
            // union by rank
            if (root1.rank < root2.rank) {
                root1.root = root2;
                root2.rank = root1.rank + 1 < root2.rank ? root1.rank + 1 : root2.rank;
            }
            else {
                root2.root = root1;
                root1.rank = root2.rank + 1 < root1.rank ? root2.rank + 1 : root1.rank;
            }
            numSet -= 1;
        }
    }


    public UFNode findRoot(UFNode node) {
        if (node.root == node)
            return node;

        // path compression
        UFNode overallRoot = findRoot(node.root);
        if (overallRoot != node.root)
            node.root = overallRoot;

        return overallRoot;
    }


    private class UFNode {
        UFNode root;
        int val;
        int rank;

        public UFNode(int val) {
            this.val = val;
            root = this;
            rank = 1;
        }
    }
}


class Solution {
    public int findCircleNum(int[][] M) {
        UnionFind uf = new UnionFind(M.length);
        for (int i = 0; i < M.length; i++) {
            for (int j = i + 1; j < M.length; j++)
                if (M[i][j] == 1)
                    uf.union(i, j);
        }

        return uf.numSet();
        // complexity: O(n^3 inverse_ackermann(n))
    }
}
