class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0)
            return 0;

        Map<Character, Integer> freqSet = new HashMap<>();

        int start = 0;
        int end = 0; // exclusive
        int ret = 0;

        while (start < s.length() && end < s.length()) {
            if (freqSet.containsKey(s.charAt(end)) || freqSet.size() < k) {
                freqSet.put(s.charAt(end), freqSet.getOrDefault(s.charAt(end), 0) + 1);
                end += 1;
            }
            else {
                ret = Math.max(ret, end - start);
                while (freqSet.size() == k && start < s.length()) {
                    if (freqSet.get(s.charAt(start)) == 1)
                        freqSet.remove(s.charAt(start));
                    else
                        freqSet.put(s.charAt(start), freqSet.get(s.charAt(start)) - 1);
                    start += 1;
                }
            }
        }

        ret = Math.max(ret, end - start);

        return ret;
    }
}
