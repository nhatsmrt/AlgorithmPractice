class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.split("\\W");
        Set<String> bannedSet = new HashSet<String>();
        for (String word : banned)
            bannedSet.add(word);
        Map<String, Integer> frequencyMap = new HashMap<String, Integer>();
        for (String word : words) {
            if (word.length() > 0) {
                word = word.toLowerCase();
                if (!bannedSet.contains(word))
                    frequencyMap.put(word, frequencyMap.getOrDefault(word, 0) + 1);
            }
        }

        String ret = "";
        int curMax = 0;
        for (String word : frequencyMap.keySet()) {
            if (frequencyMap.get(word) > curMax) {
                curMax = frequencyMap.get(word);
                ret = word;
            }
        }

        return ret;
    }
}
