class Solution {
    private Map<Integer, Integer> occur;

    public int longestSubsequence(int[] arr, int difference) {
        occur = new HashMap<Integer, Integer>();

        for (int i = arr.length - 1; i >= 0; i--)
            longestSubsequenceFrom(arr, i, difference);

        int ret = 0;
        for (int candidate : occur.values()) {
            if (candidate > ret)
                ret = candidate;
        }

        return ret;
    }

    private void longestSubsequenceFrom(int[] arr, int i, int diff) {
        int ret = 1;

        if (occur.containsKey(arr[i] + diff))
            ret += occur.get(arr[i] + diff);

        if (!occur.containsKey(arr[i]) || occur.get(arr[i]) < ret)
            occur.put(arr[i], ret);

    }
}
