class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        Map<Integer, Set<Integer>> adjacencyLists = new HashMap<Integer, Set<Integer>>();

        for (int[] edge : edges) {
            if (!adjacencyLists.containsKey(edge[0]))
                adjacencyLists.put(edge[0], new HashSet<Integer>());
            if (!adjacencyLists.containsKey(edge[1]))
                adjacencyLists.put(edge[1], new HashSet<Integer>());

            adjacencyLists.get(edge[0]).add(edge[1]);
            adjacencyLists.get(edge[1]).add(edge[0]);
        }

        Stack<Integer> traverse = new Stack<Integer>();
        Set<Integer> descendants = new LinkedHashSet<Integer>();

        int[] parent = new int[edges.length];
        traverse.push(1);
        boolean foundCycle = false;

        while (!traverse.isEmpty() && !foundCycle) {
            int cur = traverse.peek();
            if (descendants.contains(cur)) {
                descendants.remove(cur);
                traverse.pop();
            }
            else {
                descendants.add(cur);

                for (Integer neighbor : adjacencyLists.get(cur)) {
                    if (parent[cur - 1] != neighbor) {
                        if (descendants.contains(neighbor)) {
                            Iterator<Integer> it = descendants.iterator();
                            while (it.hasNext()) {
                                int value = it.next();
                                if (value != neighbor)
                                    it.remove();
                                else
                                    break;
                            }
                            foundCycle = true;
                            break;
                        }
                        else {
                            traverse.push(neighbor);
                            parent[neighbor - 1] = cur;
                        }
                    }
                }
            }
        }

        int[] ret = new int[2];
        for (int i = edges.length - 1; i >= 0; i--) {
            if (descendants.contains(edges[i][0]) && descendants.contains(edges[i][1])) {
                ret = edges[i];
                break;
            }
        }

        return ret;
    }
}
