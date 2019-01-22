class Solution {
    private int[] prefix;


    public int subarraysDivByK(int[] A, int K) {
        prefix = new int[A.length];


        prefix[0] = A[0];
        for (int i = 1; i < A.length; i++) {
            prefix[i] = prefix[i - 1] + A[i];
        }


        int ret = 0;
        for (int i = 0; i < A.length; i++) {
            for (int j = i; j < A.length; j++) {
                int remainder = (prefix[j] - prefix[i] + A[i]) % K;
                if (remainder == 0)
                    ret += 1;
            }
        }

        return ret;
    }
}
