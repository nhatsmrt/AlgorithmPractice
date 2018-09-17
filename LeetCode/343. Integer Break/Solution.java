class Solution {
    HashMap<Integer, Integer> integerBreakMap = new HashMap<Integer, Integer>();
    public int integerBreakDP(int n) {
        if (integerBreakMap.containsKey(n))
            return integerBreakMap.get(n);

        ArrayList<Integer> candidates = new ArrayList<Integer>();
        for (int i = 1; i < n; i++) {
            int dp = integerBreakDP(n - i);
            int secondPart = dp > n - i ? dp : n - i;
            int candidate = i * secondPart;
            candidates.add(candidate);
        }

        int ret = Collections.max(candidates);
        integerBreakMap.put(n, ret);
        return ret;
    }
    public int integerBreak(int n) {

        integerBreakMap.put(1, 1);
        integerBreakMap.put(2, 1);


        return integerBreakDP(n);
    }
}
