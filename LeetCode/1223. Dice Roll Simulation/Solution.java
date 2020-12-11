class Solution {
    private Map<String, Integer> dp;
    private int MOD = 1000000007;

    public int dieSimulator(int n, int[] rollMax) {
        // Time and Space Complexity: O(n * max(rollMax))

        dp = new HashMap<>();
        int ret = numWays(n, -1, 0, rollMax);
        return ret;
    }

    private int numWays(int remaining, int prevChoice, int consecChosen, int[] rollMax) {
        String key = remaining + "_" + prevChoice + "_" + consecChosen;

        if (dp.containsKey(key))
            return dp.get(key);

        int ret = 0;
        if (remaining == 0)
            ret = 1;
        else {
            for (int choice = 0; choice < rollMax.length; choice++) {
                if (choice != prevChoice || rollMax[choice] > consecChosen) {
                    if (choice == prevChoice)
                        ret += numWays(remaining - 1, choice, consecChosen + 1, rollMax);
                    else
                        ret += numWays(remaining - 1, choice, 1, rollMax);

                    ret %= MOD;
                }
            }
        }

        dp.put(key, ret);
        return ret;
    }
}
