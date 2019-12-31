class UnionFind {
    private Node[] nodes;

    public UnionFind(int n) {
        nodes = new Node[n];
        for (int i = 0; i < n; i++)
            nodes[i] = new Node(i);
    }

    public boolean union(int ind1, int ind2) {
        Node root1 = findRoot(nodes[ind1]);
        Node root2 = findRoot(nodes[ind2]);

        if (root1 == root2)
            return false;

        // union by rank:
        if (root1.rank < root2.rank)
            root1.parent = root2;
        else {
            root2.parent = root1;
            root1.rank = Math.max(root1.rank, root2.rank + 1);
        }

        return true;
    }

    private Node findRoot(Node node) {
        if (node.parent == node)
            return node;

        node.parent = findRoot(node.parent); // path compression
        return node.parent;
    }

    public boolean isConnected() {
        for (int i = 0; i < nodes.length - 1; i++) {
            if (findRoot(nodes[i]) != findRoot(nodes[i + 1]))
                return false;
        }
        return true;
    }

    private class Node {
        Node parent;
        int ind;
        int rank;

        public Node(int ind) {
            this.ind = ind;
            parent = this;
        }
    }
}


class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length >= n)
            return false;

        UnionFind uf = new UnionFind(n);
        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1]))
                return false;
        }

        return uf.isConnected();
    }
}
