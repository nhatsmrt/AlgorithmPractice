class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> firstHalf = new HashMap<Integer, Integer>();

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B.length; j++) {
                int sum = A[i] + B[j];
                if (!firstHalf.containsKey(sum))
                    firstHalf.put(sum, 1);
                else
                    firstHalf.put(sum, firstHalf.get(sum) + 1);
            }
        }

        int ret = 0;
        for (int i = 0; i < C.length; i++) {
            for (int j = 0; j < D.length; j++) {
                int sum = C[i] + D[j];
                if (firstHalf.containsKey(-sum))
                    ret += firstHalf.get(-sum);
            }
        }

        return ret;
    }
}
