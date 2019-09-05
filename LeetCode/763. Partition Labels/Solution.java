class Solution {
    public List<Integer> partitionLabels(String S) {
        List<Integer> ret = new ArrayList<Integer>();
        Map<Character, Integer> last = new HashMap<Character, Integer>();
        for (int i = 0; i < S.length(); i++) {
            last.put(S.charAt(i), i);
        }

        int cur = 0;
        int boundary = 0;
        int previousBoundary = 0;
        while (cur < S.length() && boundary < S.length()) {
            if (boundary < last.get(S.charAt(cur)))
                boundary = last.get(S.charAt(cur));
            if (cur == boundary) {
                ret.add(boundary + 1 - previousBoundary);
                previousBoundary = boundary + 1;
            }
            cur += 1;
        }

        return ret;
    }
}
