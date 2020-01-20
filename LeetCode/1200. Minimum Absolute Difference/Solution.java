class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        // O(W + N) = O(N) time complexity, O(W) = O(1) space complexity

        int minNum = 10000000;
        int maxNum = -10000000;
        for (int num : arr) {
            if (num < minNum)
                minNum = num;

            if (maxNum < num)
                maxNum = num;
        }
        int[] cnt = new int[maxNum - minNum + 1];
        for (int num : arr)
            cnt[num - minNum] += 1;

        int ind = 0;
        for (int i = 0; i < maxNum - minNum + 1; i++) {
            for (int j = 0; j < cnt[i]; j++) {
                arr[ind] = i + minNum;
                ind += 1;
            }
        }

        List<List<Integer>> ret = new ArrayList<>();

        int minDiff = 10000000;
        for (int i = 0; i < arr.length - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (minDiff > diff)
                minDiff = diff;
        }

        for (int i = 0; i < arr.length - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (diff == minDiff)
                addPair(ret, arr[i], arr[i + 1]);
        }

        return ret;
    }

    private void addPair(List<List<Integer>> ret, int a, int b) {
        List<Integer> pair = new ArrayList<>();
        pair.add(a);
        pair.add(b);
        ret.add(pair);
    }
}
