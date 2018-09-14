class Solution {
    public int numTreesDP(int n, int[] numUniqueTree) {
        if (numUniqueTree[n] != 0)
            return numUniqueTree[n];

        if (n == 0 || n == 1) {
            numUniqueTree[n] = 1;
            return 1;
        }

        Integer ret = new Integer(0);
        for (int i = 0; i < n; i++) {
            ret += numTreesDP(i, numUniqueTree) * numTreesDP(n - 1 - i, numUniqueTree);
        }

        numUniqueTree[n] = ret;
        return ret;
    }

    public int numTrees(int n) {
        int[] numUniqueTree = new int[n + 1];
        Arrays.fill(numUniqueTree, 0);
        return numTreesDP(n, numUniqueTree);
    }
}
