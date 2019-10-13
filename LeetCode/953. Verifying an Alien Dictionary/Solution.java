class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> orderMap = new HashMap<Character, Integer>();
        for (int i = 0; i < order.length(); i++)
            orderMap.put(order.charAt(i), i);

        for (int i = 1; i < words.length; i++) {
            if (!compare(words[i - 1], words[i], orderMap))
                return false;
        }

        return true;
    }

    private boolean compare(String word1, String word2, Map<Character, Integer> orderMap) {
        // return true if word1 <= word2, false otherwise
        int i = 0;
        while (i < word1.length() && i < word2.length() && word1.charAt(i) == word2.charAt(i))
            i += 1;

        if (i == word1.length())
            return i <= word2.length();

        if (i == word2.length())
            return i == word1.length();

        return orderMap.get(word1.charAt(i)) < orderMap.get(word2.charAt(i));
    }
}
