class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // Time and Space Complexity: O(n)

        // Let gain[i] = gas[i] - cost[i]
        // we want to find an i such that
        // gain[i], gain[i] + gain[(i + 1)%n],... >= 0

        int[] cyclicPrefixSum = new int[gas.length * 2 + 1];
        for (int i = 1; i < gas.length * 2 + 1; i++)
            cyclicPrefixSum[i] = cyclicPrefixSum[i - 1] +
            gas[(i - 1) % gas.length] - cost[(i - 1) % gas.length];

        // In order for gain[i], gain[i] + gain[(i + 1)%n],... >= 0
        // We need cyclicPrefixSum[i + 1] >= cyclicPrefixSum[i], ...,
        // cyclicPrefixSum[i + n] >= cyclicPrefixSum[i]
        // Let RNSV[i] = j > i if cyclicPrefixSum[i] > cyclicPrefixSum[j] and
        // cyclicPrefixSum[i] <= k for all i <= k < j.
        // Then the condition is satisfied when RNSV[i] - i > n

        int rnsv[] = new int[cyclicPrefixSum.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = cyclicPrefixSum.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() &&
                   cyclicPrefixSum[stack.peek()] >= cyclicPrefixSum[i])
                stack.pop();
            if (stack.isEmpty())
                rnsv[i] = cyclicPrefixSum.length;
            else
                rnsv[i] = stack.peek();
            stack.push(i);
        }

        for (int i = 1; i < gas.length + 1; i++) {
            if (rnsv[i] - i > gas.length)
                return i % gas.length;
        }

        return -1;
    }
}
