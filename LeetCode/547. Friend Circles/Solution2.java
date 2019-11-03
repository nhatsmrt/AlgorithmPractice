class Solution2 {
    public int findCircleNum(int[][] M) {
        // time complexity: O(n^2)
        Set<Integer> remaining = new HashSet<Integer>();
        Map<Integer, Set<Integer>> adjLists = new HashMap<Integer, Set<Integer>>();
        int ret = 0;

        for (int i = 0; i < M.length; i++) {
            remaining.add(i);
            adjLists.put(i, new HashSet<Integer>());

            for (int j = 0; j < i; j++) {
                if (M[i][j] == 1) {
                    adjLists.get(i).add(j);
                    adjLists.get(j).add(i);
                }
            }
        }

        while (!remaining.isEmpty()) {
            int node = remaining.iterator().next();
            ret += 1;
            dfs(node, remaining, adjLists);
        }

        return ret;
    }

    private void dfs(int node, Set<Integer> remaining, Map<Integer, Set<Integer>> adjLists) {
        remaining.remove(node);
        for (Integer next : adjLists.get(node)) {
            if (remaining.contains(next))
                dfs(next, remaining, adjLists);
        }
    }
}
