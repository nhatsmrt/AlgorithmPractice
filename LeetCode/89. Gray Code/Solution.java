class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> ret = new ArrayList<Integer>();
        ret.add(0);

        int numCodes = (int) Math.pow(2.0, n);
        int ind = 1;
        while (ind < numCodes) {
            ret.add(ind ^ (ind >> 1));
            ind += 1;
        }

        return ret;
    }
}
