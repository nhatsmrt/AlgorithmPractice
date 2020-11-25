class Solution {
public:
    int smallestRepunitDivByK(int K) {
        // Time Complexity: O(K)
        // Space Complexity: O(1)

        if (K == 1)
            return 1;

        if (K % 2 == 0 || K % 5 == 0)
            return -1;


        int remainder = 0;
        for (int num_digs = 1; num_digs < K + 1; num_digs++) {
            remainder = (remainder * 10 + 1) % K;

            if (remainder == 0)
                return num_digs;
        }

        return -1;
    }
};
