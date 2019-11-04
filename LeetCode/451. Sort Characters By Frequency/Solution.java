class Solution {
    public String frequencySort(String s) {
        // complexity: O(n + maxCount)
        if (s.length() <= 2)
            return s;

        Map<Character, Integer> charCount = new HashMap<Character, Integer>();
        int maxCnt = 1;

        for (int i = 0; i < s.length(); i++) {
            if (!charCount.containsKey(s.charAt(i)))
                charCount.put(s.charAt(i), 1);
            else {
                int cnt = charCount.get(s.charAt(i)) + 1;
                charCount.put(s.charAt(i), cnt);
                if (cnt > maxCnt)
                    maxCnt = cnt;
            }
        }

        Map<Integer, Set<Character>> sortedCharCount = new HashMap<Integer, Set<Character>>();
        for (Character c : charCount.keySet()) {
            int cnt =  charCount.get(c);
            if (!sortedCharCount.containsKey(cnt))
                sortedCharCount.put(cnt, new HashSet<Character>());
            sortedCharCount.get(cnt).add(c);
        }

        StringBuilder ret = new StringBuilder();
        for (int cnt = maxCnt; cnt >= 0; cnt--) {
            if (sortedCharCount.containsKey(cnt)) {
                Set<Character> chars = sortedCharCount.get(cnt);
                for (Character c : chars) {
                    for (int i = 0; i < cnt; i++)
                        ret.append(c);
                }
            }
        }

        return ret.toString();

    }
}
