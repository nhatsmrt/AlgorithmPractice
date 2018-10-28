class Solution {
    private Map<String, Boolean> dpMap;

    private boolean wordBreakDP(String s, List<String> wordDict) {
        if (dpMap.containsKey(s))
            return dpMap.get(s);

        for (String word : wordDict) {
            if (matchPrefix(s, word)) {
                if (wordBreakDP(s.substring(word.length()), wordDict)) {
                    dpMap.put(s, true);
                    return true;
                }
            }
        }

        dpMap.put(s, false);
        return false;
    }

    private boolean matchPrefix(String s, String prefix) {
        if (s.length() < prefix.length())
            return false;

        return s.substring(0, prefix.length()).equals(prefix);
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        dpMap = new HashMap<String, Boolean>();
        for (String word : wordDict)
            dpMap.put(word, true);

        return wordBreakDP(s, wordDict);
    }
}
