class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<List<Integer>>> adjLists = new HashMap<Integer, List<List<Integer>>>();
        int[] dist = new int[N];
        Set<Integer> unvisited = new HashSet<Integer>();

        for (int i = 0; i < N; i++) {
            adjLists.put(i, new ArrayList<List<Integer>>());
            dist[i] = 6000000;
            unvisited.add(i);
        }
        dist[K - 1] = 0;

        for (int[] edge : times) {
            List<Integer> edgeList = new ArrayList<Integer>();
            edgeList.add(edge[1] - 1);
            edgeList.add(edge[2]);

            adjLists.get(edge[0] - 1).add(edgeList);
        }


        while(!unvisited.isEmpty()) {
            int curMinDist = 6000000;
            Integer curNode = -1;
            for (Integer node : unvisited) {
                if (dist[node] < curMinDist) {
                    curNode = node;
                    curMinDist = dist[node];
                }
            }
            if (curNode == -1)
                break;

            unvisited.remove(curNode);

            for (List<Integer> edge : adjLists.get(curNode)) {
                if (unvisited.contains(edge.get(0)) &&
                    dist[edge.get(0)] > edge.get(1) + dist[curNode]
                   )
                    dist[edge.get(0)] = edge.get(1) + dist[curNode];
            }
        }

        int maxTime = 0;
        for (int i = 0; i < N; i++) {
            if (maxTime < dist[i])
                maxTime = dist[i];
        }

        if (maxTime < 6000000)
            return maxTime;
        else
            return -1;
    }
}
