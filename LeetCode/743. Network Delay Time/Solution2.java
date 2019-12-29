class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        // Dial's algorithm
        // Time Complexity: O(W|V| + |E|)

        Map<Integer, Map<Integer, Integer>> adjLists = new HashMap<>();
        int[] dists = new int[N + 1];
        Arrays.fill(dists, -1);
        dists[K] = 0;

        for (int[] edge : times) {
            if(!adjLists.containsKey(edge[0]))
                adjLists.put(edge[0], new HashMap<>());
            adjLists.get(edge[0]).put(edge[1], edge[2]);
        }

        List<Set<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i < N * 100 + 1; i++)
            buckets.add(new HashSet<Integer>());
        buckets.get(0).add(K);

        for (int i = 0; i < N * 100 + 1; i++) {
            Set<Integer> bucket = buckets.get(i);
            while (!bucket.isEmpty()) {
                Iterator<Integer> it = bucket.iterator();
                Integer node = it.next();
                it.remove();

                if (adjLists.containsKey(node)) {
                    Map<Integer, Integer> neighbors = adjLists.get(node);
                    for (Integer neighbor : neighbors.keySet()) {
                        int candidateDist = i + neighbors.get(neighbor);
                        if (dists[neighbor] == -1) {
                            dists[neighbor] = candidateDist;
                            buckets.get(dists[neighbor]).add(neighbor);
                        }
                        else if (candidateDist < dists[neighbor]) {
                            buckets.get(dists[neighbor]).remove(neighbor);
                            dists[neighbor] = candidateDist;
                            buckets.get(dists[neighbor]).add(neighbor);
                        }
                    }
                }
            }
        }

        int ret = 0;
        for (int i = 1; i <= N; i++) {
            if (dists[i] == -1)
                return -1;
            ret = Math.max(ret, dists[i]);
        }

        return ret;
    }
}
