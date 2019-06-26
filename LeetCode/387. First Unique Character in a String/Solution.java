class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> charMap = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!charMap.containsKey(c)) {
                charMap.put(c, i);
            }
            else {
                charMap.put(c, -1);
            }
        }

        int ind = -1;
        for (Character c : charMap.keySet()) {
            if (charMap.get(c) >= 0) {
                if (ind < 0 || charMap.get(c) < ind)
                    ind = charMap.get(c);
            }
        }

        return ind;
    }
}
