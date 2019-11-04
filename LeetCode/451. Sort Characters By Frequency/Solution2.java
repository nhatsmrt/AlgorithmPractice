class Solution {
    public String frequencySort(String s) {
        // complexity: O(n log n)
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

        PriorityQueue<Character> queue = new PriorityQueue<Character>(new CharComparator(charCount));
        for (Character c : charCount.keySet())
            queue.add(c);

        StringBuilder ret = new StringBuilder();
        while (!queue.isEmpty()) {
            char c = queue.poll();
            int cnt = charCount.get(c);
            for (int i = 0; i < cnt; i++)
                ret.append(c);
        }


        return ret.toString();

    }

    private class CharComparator implements Comparator<Character> {
        Map<Character, Integer> charCount;

        public CharComparator(Map<Character, Integer> charCount) {
            this.charCount = charCount;
        }

        public int compare(Character c1, Character c2) {
            return -Integer.compare(charCount.get(c1), charCount.get(c2));
        }
    }
}
