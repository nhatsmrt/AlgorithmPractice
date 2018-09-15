import java.math.BigInteger;
class Solution {
    HashMap<BigInteger, Integer> decodings = new HashMap<BigInteger, Integer>();
    BigInteger TEN = new BigInteger("10");
    BigInteger ZERO = new BigInteger("0");
    BigInteger HUND = new BigInteger("100");
    BigInteger TS = new BigInteger("26");

    public boolean isDivisible(BigInteger a, BigInteger b) {
        return a.mod(b).equals(ZERO);
    }
    public int numDecodingsDP(BigInteger num) {
        if (decodings.containsKey(num))
            return decodings.get(num);

        if (isDivisible(num, HUND)) {
            decodings.put(num, 0);
            return 0;
        }

        if (isDivisible(num, TEN)) {
            if (num.mod(HUND).compareTo(TS) > 0) {
                decodings.put(num, 0);
                return 0;
            }
            else {
                decodings.put(num, numDecodingsDP(num.divide(HUND)));
                return decodings.get(num);
            }
        }

        int subCase1 = numDecodingsDP(num.divide(TEN));
        int subCase2;
        if (num.mod(HUND).compareTo(TS) <= 0 & !isDivisible(num.divide(TEN), TEN))
            subCase2 = numDecodingsDP(num.divide(HUND));
        else
            subCase2 = 0;

        decodings.put(num, subCase1 + subCase2);
        return decodings.get(num);

    }
    public int numDecodings(String s) {
        if (s.equals("") || s.charAt(0) == '0')
            return 0;

        BigInteger num = new BigInteger(s);

        for (int i = 0; i < 10; i++)
            decodings.put(new BigInteger(Integer.toString(i)), 1);

        return numDecodingsDP(num);
    }
}
