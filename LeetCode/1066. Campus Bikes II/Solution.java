class Solution {
    private int[][] distances;
    private Map<BitSet, Integer> dpMap;

    public int assignBikes(int[][] workers, int[][] bikes) {
        distances = new int[workers.length][bikes.length];
        for (int i = 0; i < workers.length; i++) {
            for (int j = 0; j < bikes.length; j++) {
                distances[i][j] = manhatDist(workers[i], bikes[j]);
            }
        }

        dpMap = new HashMap<BitSet, Integer>();
        BitSet state = new BitSet(bikes.length);

        return assignBikes(state);
    }

    private int assignBikes(BitSet state) {
        if (dpMap.containsKey(state))
            return dpMap.get(state);

        int worker = state.cardinality();
        if (worker >= distances.length)
            return 0;

        int ret = -1;
        for (int bike = 0; bike < distances[0].length; bike++) {
            if (!state.get(bike)) {
                BitSet nextState = (BitSet) state.clone();
                nextState.set(bike);
                int candidate = distances[worker][bike] + assignBikes(nextState);
                if (ret == -1 || candidate < ret)
                    ret = candidate;
            }
        }
        dpMap.put(state, ret);
        return ret;
    }


    private int manhatDist(int[] worker, int[] bike) {
        return Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
    }
}
