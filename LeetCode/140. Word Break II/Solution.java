class Solution {
    private Map<String, List<String>> dpMap;

    public List<String> wordBreak(String s, List<String> wordDict) {
        dpMap = new HashMap<String, List<String>>();
        return wordBreakDP(s, wordDict);
    }

    private List<String> wordBreakDP(String s, List<String> wordDict) {
        if (dpMap.containsKey(s))
            return dpMap.get(s);

        List<String> ret = new ArrayList<String>();
        if (s.equals("")) {
            ret.add(s);
            return ret;
        }

        for (String prefix : wordDict) {
            if (s.indexOf(prefix) == 0) {
                List<String> rightHalf = wordBreakDP(s.substring(prefix.length()), wordDict);
                for (String words : rightHalf) {
                    if (words.equals(""))
                        ret.add(prefix);
                    else
                        ret.add(prefix + " " + words);
                }
            }
        }

        dpMap.put(s, ret);
        return ret;
    }


}
