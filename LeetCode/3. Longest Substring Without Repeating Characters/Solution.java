class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0)
            return 0;

        Set<Character> curChar = new HashSet<Character>();
        curChar.add(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            if (curChar.contains(s.charAt(i)))
                break;
            else
                curChar.add(s.charAt(i));
        }

        int maxLen = curChar.size();
        if (maxLen == s.length())
            return maxLen;

        for (int i = 1; i < s.length(); i++) {
            curChar.remove(s.charAt(i - 1));
            int curInd = i + curChar.size();
            while (curInd < s.length() && !curChar.contains(s.charAt(curInd))) {
                curChar.add(s.charAt(curInd));
                curInd += 1;
            }

            if (curChar.size() > maxLen)
                maxLen = curChar.size();

            if (curInd == s.length())
                break;
        }

        return maxLen;


    }
}
