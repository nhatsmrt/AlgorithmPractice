class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ret = new ArrayList<Integer>();
        ret.add(1);
        if (rowIndex == 0)
            return ret;

        int cur = 1;

        for (int i = 0; i < rowIndex / 2; i++) {
            if (cur % (i + 1) == 0) {
                cur /= i + 1;
                cur *= rowIndex - i;
            }
            else if (cur * (rowIndex - i) > 0) {
                cur *= rowIndex - i;
                cur /= i + 1;
            }
            else {
                int half1 = cur / 2;
                int half2 = cur - half1;
                half1 *= (rowIndex - i);
                half2 *= (rowIndex - i);

                cur = half1 / (i + 1) + half2 / (i + 1) + 1;
            }

            ret.add(cur);
        }
        for (int i = (rowIndex - 1) / 2; i >= 0; i--) {
            ret.add(ret.get(i));
        }

        return ret;
    }
}
