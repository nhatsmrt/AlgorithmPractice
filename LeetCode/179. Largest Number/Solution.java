import java.math.*;

class Solution {
    public String largestNumber(int[] nums) {
        if (nums.length == 0)
            return "0";

        ArrayList<Integer> numList = new ArrayList<Integer>();

        for (int i = 0; i < nums.length; i++)
            numList.add(nums[i]);

        Collections.sort(numList, new LexicoOrder());
        String ret = "";

        if (numList.get(0) == 0)
            return "0";

        for (int i = 0; i < numList.size(); i++)
            ret += numList.get(i);

        return ret;
    }


    class LexicoOrder implements Comparator<Integer> {
        public int compare(Integer first, Integer second) {
            String firstStr = first.toString();
            String secondStr = second.toString();

            String concat1 = firstStr + secondStr;
            String concat2 = secondStr + firstStr;

            BigInteger concatInt1 =  new BigInteger(concat1);
            BigInteger concatInt2 =  new BigInteger(concat2);

            return concatInt2.compareTo(concatInt1);
        }

    }
}
