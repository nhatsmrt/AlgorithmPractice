class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        // Time Complexity: O(K|E|) (K iterations of Bellman-Ford)
        // Space Complexity: O(n)
        int INF = 1000000000;

        int[][] minDist = new int[2][n];
        Arrays.fill(minDist[0], INF);
        Arrays.fill(minDist[1], INF);

        minDist[0][src] = minDist[1][src] = 0;

        for (int i = 0; i < K + 1; i++) {
            for (int[] flight : flights) {
                // attempt to relax
                minDist[i & 1][flight[1]] = Math.min(
                    minDist[i & 1][flight[1]],
                    minDist[1 - (i & 1)][flight[0]] + flight[2]
                );
            }
        }

        return  minDist[K & 1][dst] == INF ? -1 : minDist[K & 1][dst];
    }
}
