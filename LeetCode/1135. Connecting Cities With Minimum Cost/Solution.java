class UnionFind {
    Map<Integer, UFNode> nodesMap;
    int numComponents;

    public UnionFind(int N) {
        nodesMap = new HashMap<Integer, UFNode>();
        for (int i = 1; i <= N; i++)
            nodesMap.put(i, new UFNode(i));
        numComponents = N;
    }

    public void union(int val1, int val2) {
        UFNode root1 = find(nodesMap.get(val1));
        UFNode root2 = find(nodesMap.get(val2));

        if (root1 != root2) {
            // union by rank
            if (root1.rank < root2.rank) {
                root1.root = root2;
                root2.rank = Math.max(root1.rank + 1, root2.rank);
            }
            else {
                root2.root = root1;
                root1.rank = Math.max(root2.rank + 1, root1.rank);
            }
            numComponents -= 1;
        }
    }


    public int find(int val) {
        UFNode node = nodesMap.get(val);
        return find(node).val;
    }

    private UFNode find(UFNode node) {
        if (node.root == node)
            return node;

        UFNode root = find(node.root);
        // path compression
        node.root = root;
        return root;
    }

    public boolean isConnected() {
        return numComponents == 1;
    }


    public class UFNode {
        int val;
        UFNode root;
        int rank;

        public UFNode(int val) {
            this.val = val;
            root = this;
            rank = 1;
        }
    }
}


class Solution {
    public int minimumCost(int N, int[][] connections) {
        Arrays.sort(connections, new Comparator<int[]>() {
            public int compare(int[] edge1, int[] edge2) {
                return edge1[2] - edge2[2];
            }
        });

        int ret = 0;
        UnionFind uf = new UnionFind(N);
        for (int[] edge : connections) {
            if (uf.find(edge[0]) != uf.find(edge[1])) {
                ret += edge[2];
                uf.union(edge[0], edge[1]);
            }
        }

        if (uf.isConnected())
            return ret;
        return -1;
    }
}
