class Solution {
    public boolean isBipartite(int[][] graph) {
        int numVertices = graph.length;

        if (numVertices == 0)
            return true;

        int[] part = new int[numVertices];
        Arrays.fill(part, -1);
        ArrayDeque<Integer> traverseDeque = new ArrayDeque<Integer>();
        ArrayDeque<Integer> remainingNodes = new ArrayDeque<Integer>();

        int numNodeReached = 0;


        boolean notFound = false;

        while (numNodeReached < numVertices) {
            if (traverseDeque.isEmpty()) {
                for (int i = 0; i < numVertices; i++) {
                    if (part[i] == -1 && (graph[i].length != 0)) {
                        part[i] = 0;
                        traverseDeque.addLast(i);
                        numNodeReached += 1;
                        break;
                    }
                    else if (i == numVertices - 1)
                        notFound = true;
                }
            }

            if (notFound)
                break;

            int node = traverseDeque.pop();
            for (int neighbor : graph[node]) {
                if (part[neighbor] != -1) {
                    if (part[neighbor] + part[node] != 1)
                        return false;
                }
                else {
                    part[neighbor] = 1 - part[node];
                    traverseDeque.addLast(neighbor);
                }
            }
            numNodeReached += 1;
        }


        return true;


    }
}
