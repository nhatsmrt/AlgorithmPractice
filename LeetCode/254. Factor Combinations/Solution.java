class Solution {
    public List<List<Integer>> getFactors(int n) {
        return getFactors(2, n);
    }

    private List<List<Integer>> getFactors(int lowerBound, int n) {
        List<List<Integer>> ret = new ArrayList<>();
        int upperBound = (int) Math.sqrt(n);
        for (int i = lowerBound; i <= upperBound; i++) {
            if (n % i == 0) {
                List<List<Integer>> subfactors = getFactors(i, n / i);
                List<Integer> factor = new ArrayList<>();
                factor.add(i);
                factor.add(n / i);
                ret.add(factor);
                for (List<Integer> subfactor : subfactors) {
                    subfactor.add(i);
                    ret.add(subfactor);
                }
            }
        }

        return ret;
    }
}
