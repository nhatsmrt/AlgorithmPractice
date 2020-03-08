class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> ret = new ArrayList<>(n);
        for (int i = 1; i < 10; i++)
            build(i, n, ret);
        return ret;
    }

    private void build(int cur, int bound, List<Integer> ret) {
        if (cur <= bound) {
            ret.add(cur);
            for (int i = 0; i < 10; i++)
                build(cur * 10 + i, bound, ret);
        }
    }
}
