import java.math.BigInteger;
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        int setSize = nums.length;
        BigInteger ONE = new BigInteger("1");
        BigInteger powerSetSize = ONE.shiftLeft(setSize);
        BigInteger it = new BigInteger("0");

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        while (it.compareTo(powerSetSize) < 0) {
            ArrayList<Integer> subset = new ArrayList<Integer>();

            String binaryCode = it.toString(2);
            int codeLen = binaryCode.length();
            for (int i = codeLen - 1; i >= 0; i--) {
                if (binaryCode.charAt(i) == '1')
                    subset.add(0, nums[setSize - (codeLen - i)]);
            }

            ret.add(subset);
            it = it.add(ONE);
        }

        return ret;
    }
}
