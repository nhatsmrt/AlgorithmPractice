class Solution {
    private void dailyTemperaturesRecursive(int[] ret, int[] T, int ind, int query) {
        if (T[ind] == T[query])
            ret[ind] = ret[query] == 0 ? 0 : ret[query] + query - ind;
        else if (T[ind] < T[query])
            ret[ind] = query - ind;
        else if (ret[query] == 0)
            ret[ind] = 0;
        else
            dailyTemperaturesRecursive(ret, T, ind, query + ret[query]);


    }

    public int[] dailyTemperatures(int[] T) {
        int[] ret = new int[T.length];
        Arrays.fill(ret, 0);

        for (int i = T.length - 2; i >= 0; i--) {
            dailyTemperaturesRecursive(ret, T, i, i + 1);
        }

        return ret;
    }
}
