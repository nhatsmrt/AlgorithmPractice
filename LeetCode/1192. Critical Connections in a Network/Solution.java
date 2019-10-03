class Solution {
    private int curPreorder;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Node[] graph = new Node[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new Node(i);
        }

        for (List<Integer> edge : connections) {
            graph[edge.get(0)].adjList.add(graph[edge.get(1)]);
            graph[edge.get(1)].adjList.add(graph[edge.get(0)]);
        }

        Node first = graph[0];
        curPreorder = 0;
        DFS(first, ret);
        return ret;

    }


    private void DFS(Node node, List<List<Integer>> ret) {
        node.preorder = node.lowlink = curPreorder;
        curPreorder += 1;

        for (Node child : node.adjList) {
            if (child.preorder == -1) {
                child.par = node;
                DFS(child, ret);
                if (child.lowlink < node.lowlink)
                    node.lowlink = child.lowlink;
            }
            else if (node.lowlink > child.preorder && node.par != child)
                node.lowlink = child.preorder;
        }

        for (Node child : node.adjList) {
            if (child.preorder > node.preorder && child.lowlink > node.preorder) {
                List<Integer> edge = new ArrayList<Integer>();
                edge.add(node.value);
                edge.add(child.value);
                ret.add(edge);
            }
        }
    }


    private class Node {
        int value;
        int lowlink;
        int preorder;
        List<Node> adjList;
        Node par;

        public Node(int value) {
            this.value = value;
            lowlink = -1;
            preorder = -1;
            adjList = new ArrayList<Node>();
        }
    }
}
