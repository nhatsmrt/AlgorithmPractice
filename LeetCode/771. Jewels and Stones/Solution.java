class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jewels = new HashSet<Character>();
        for (int i = 0; i < J.length(); i++)
            jewels.add(J.charAt(i));

        int ret = 0;
        for (int i = 0; i < S.length(); i++) {
            if (jewels.contains(S.charAt(i)))
                ret += 1;
        }

        return ret;

    }
}
