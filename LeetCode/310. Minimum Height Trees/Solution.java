class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n < 3) {
            ArrayList<Integer> ret = new ArrayList<Integer>();

            for (int i = 0; i < n; i++)
                ret.add(i);

            return ret;
        }

        ArrayList<ArrayList<Integer>> neighborList = new ArrayList<ArrayList<Integer>>();
        int[] degree = new int[n];
        boolean[] visited = new boolean[n];

        int nodesRemained = n;


        Arrays.fill(degree, 0);
        Arrays.fill(visited, false);
        for (int i = 0; i < n; i++)
            neighborList.add(new ArrayList<Integer>());


        for (int[] edge : edges) {
            neighborList.get(edge[0]).add(edge[1]);
            neighborList.get(edge[1]).add(edge[0]);

            degree[edge[0]] += 1;
            degree[edge[1]] += 1;
        }


        ArrayDeque<Integer> traverseDeque = new ArrayDeque<Integer>();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 1) {
                traverseDeque.addLast(i);
                visited[i] = true;
            }
        }

        while (nodesRemained > 2) {
            int numLeafNode = traverseDeque.size();
            for (int i = 0; i < numLeafNode; i++) {
                Integer node = traverseDeque.pop();
                for (Integer neighbor : neighborList.get(node)) {
                    if (!visited[neighbor]) {
                        degree[neighbor] -= 1;

                        if (degree[neighbor] == 1) {
                            traverseDeque.add(neighbor);
                            visited[neighbor] = true;
                        }
                    }
                }
                nodesRemained -= 1;
            }
        }

        ArrayList<Integer> ret = new ArrayList<Integer>();
        while (!traverseDeque.isEmpty()) {
            ret.add(traverseDeque.pop());
        }

        return ret;
    }
}
