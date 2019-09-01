class Solution {
    class UnionFind<T> {
        private Map<T, UFNode> nodes;

        public UnionFind() {
            nodes = new HashMap<T, UFNode>();
        }

        public void union(T c1, T c2) {
            if (c1 != c2) {
                UFNode node1 = findRoot(nodes.get(c1));
                UFNode node2 = findRoot(nodes.get(c2));

                if (node1 != node2) {
                    if (node1.rank < node2.rank) {
                        node1.par = node2;
                        // node2.rank += node1.rank;
                        node2.rank = node1.rank + 1 < node2.rank ? node1.rank + 1 : node2.rank;
                    }
                    else {
                        node2.par = node1;
                        node1.rank = node2.rank + 1 < node1.rank ? node2.rank + 1 : node1.rank;
                        // node1.rank += node2.rank;
                    }
                }

            }
        }

        public T find(T c) {
            UFNode<T> node = findRoot(nodes.get(c));
            return node.value;
        }

        private UFNode<T> findRoot(UFNode<T> node) {
            if (node.par == node)
                return node;
            else {
                // path compression
                UFNode<T> root = findRoot(node.par);
                if (root != node.par)
                    node.par = root;
                return root;
            }
        }

        public void add(T c) {
            if (!nodes.containsKey(c))
                nodes.put(c, new UFNode<T>(c));
        }

        public void print() {
            for (UFNode node : nodes.values()) {
                System.out.println(node.value);
                if (node.par != null && node.par != node)
                    System.out.println(node.par.value);
                else
                    System.out.println(node.value);
                System.out.println(node.rank);
                System.out.println();
            }

        }


        class UFNode<T> {
            int rank;
            T value;
            UFNode par;

            public UFNode(T value) {
                this.value = value;
                par = this;
                rank = 1;
            }
        }
    }

    public boolean equationsPossible(String[] equations) {
        Set<String> ineq = new HashSet<String>();
        UnionFind<Character> uf = new UnionFind<Character>();

        for (String equation : equations) {
            uf.add(equation.charAt(0));
            uf.add(equation.charAt(3));

            if (equation.charAt(1) == '=') {
                uf.union(equation.charAt(0), equation.charAt(3));
            }
            else
                ineq.add(equation);
        }

        if (ineq.size() == 0)
            return true;


        for (String e : ineq) {
            if (uf.find(e.charAt(0)) == uf.find(e.charAt(3)))
                return false;
        }

        return true;
    }
}
