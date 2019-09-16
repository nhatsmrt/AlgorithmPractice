class UnionFind {
    Map<Integer, UFNode> nodesMap;

    public UnionFind() {
        nodesMap = new HashMap<Integer, UFNode>();
    }

    public boolean union (int value1, int value2) {
        if (value1 != value2) {
            UFNode root1 = findRoot(nodesMap.get(value1));
            UFNode root2 = findRoot(nodesMap.get(value2));

            if (root1 != root2) {
                // union by rank:
                if (root1.rank < root2.rank) {
                    root1.par = root2;
                    root2.rank += root1.rank;
                }
                else {
                    root2.par = root1;
                    root1.rank += root2.rank;
                }
                return true;
            }
        }

        return false;
    }

    public int find(int value) {
        UFNode ret = findRoot(nodesMap.get(value));
        return ret.value;
    }

    public UFNode findRoot(UFNode node) {
        if (node.par == node)
            return node;
        else {
            UFNode root = findRoot(node.par);
            node.par = root; // path compression
            return root;
        }
    }

    public boolean add(int value) {
        if (!nodesMap.containsKey(value)) {
            nodesMap.put(value, new UFNode(value));
            return true;
        }
        return false;
    }

    class UFNode {
        int rank;
        int value;
        UFNode par;

        public UFNode(int value) {
            rank = 1;
            par = this;
            this.value = value;
        }
    }
}


class Solution2 {
    public int[] findRedundantConnection(int[][] edges) {
        UnionFind uf = new UnionFind();
        for (int i = 1; i < edges.length + 1; i++)
            uf.add(i);

        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1]))
                return edge;
        }

        return new int[2];
    }
}
