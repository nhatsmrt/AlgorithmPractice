class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character, Integer> wordCnt = new HashMap<>();
        int begin = 0;

        int length = 0;
        int i = 0;

        while (i < s.length()) {
            if (wordCnt.containsKey(s.charAt(i)) || wordCnt.size() < 2) {
                wordCnt.put(s.charAt(i), wordCnt.getOrDefault(s.charAt(i), 0) + 1);
                i++;
            }
            else {
                if ((i - begin) > length) {
                    length = i - begin;
                }

                while (wordCnt.size() == 2) {
                    if (wordCnt.get(s.charAt(begin)) == 1)
                        wordCnt.remove(s.charAt(begin));
                    else
                        wordCnt.put(s.charAt(begin), wordCnt.get(s.charAt(begin)) - 1);
                    begin++;
                }

            }
        }

        return Math.max(length, i - begin);
    }
}
