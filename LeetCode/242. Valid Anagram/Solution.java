class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charCount1 = new int[26];
        int[] charCount2 = new int[26];

        for (int i = 0; i < s.length(); i++)
            charCount1[(int) (s.charAt(i) - 'a')] += 1;

        for (int i = 0; i < t.length(); i++)
            charCount2[(int) (t.charAt(i) - 'a')] += 1;

        for (int i = 0; i < 26; i++) {
            if (charCount1[i] != charCount2[i])
                return false;
        }

        return true;

    }

    public boolean isAnagramV2(String s, String t) {
        if (s.length() != t.length())
            return false;

        if (s.length() == 0)
            return true;

        Map<Character, Integer> charCount1 = new HashMap<Character, Integer>();
        Map<Character, Integer> charCount2 = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            if (!charCount1.containsKey(s.charAt(i)))
                charCount1.put(s.charAt(i), 1);
            else
                charCount1.put(s.charAt(i), charCount1.get(s.charAt(i)) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            if (!charCount2.containsKey(t.charAt(i)))
                charCount2.put(t.charAt(i), 1);
            else
                charCount2.put(t.charAt(i), charCount2.get(t.charAt(i)) + 1);
        }

        return charCount1.equals(charCount2);

    }
}
