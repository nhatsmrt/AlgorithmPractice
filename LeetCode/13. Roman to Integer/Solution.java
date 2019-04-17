class Solution {
    private Map<String, Integer> digits;

    public int romanToInt(String s) {
        digits = new HashMap<String, Integer>() {
            {
                put("I", 1);
                put("V", 5);
                put("X", 10);
                put("L", 50);
                put("C", 100);
                put("D", 500);
                put("M", 1000);
            }
        };

        return romanToIntHelper(s);
    }

    private int romanToIntHelper(String s) {
        if (s.length() == 0)
            return 0;

        if (s.length() == 1)
            return digits.get(s);

        if (s.charAt(0) == 'I' && s.charAt(1) == 'V')
            return 4 + romanToIntHelper(s.substring(2));

        if (s.charAt(0) == 'I' && s.charAt(1) == 'X')
            return 9 + romanToIntHelper(s.substring(2));

        if (s.charAt(0) == 'X' && s.charAt(1) == 'L')
            return 40 + romanToIntHelper(s.substring(2));

        if (s.charAt(0) == 'X' && s.charAt(1) == 'C')
            return 90 + romanToIntHelper(s.substring(2));

        if (s.charAt(0) == 'C' && s.charAt(1) == 'D')
            return 400 + romanToIntHelper(s.substring(2));

        if (s.charAt(0) == 'C' && s.charAt(1) == 'M')
            return 900 + romanToIntHelper(s.substring(2));


        return digits.get(s.substring(0, 1)) + romanToIntHelper(s.substring(1));

    }
}
