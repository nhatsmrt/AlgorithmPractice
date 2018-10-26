class Solution {
    private Map<Integer, List<String>> dpMap;

    private List<String> generateParenthesisDP(int n) {
        if (dpMap.containsKey(n))
            return dpMap.get(n);

        List<String> ret = new LinkedList<String>();

        for (int i = 0; i < n; i++) {
            List<String> left = generateParenthesisDP(i);
            List<String> right = generateParenthesisDP(n - 1 - i);

            for (String firstHalf : left) {
                for (String secondHalf : right) {
                    String concat = "(" + firstHalf + ")" + secondHalf;
                    ret.add(concat);
                }
            }
        }

        dpMap.put(n, ret);
        return ret;

    }

    public List<String> generateParenthesis(int n) {
        dpMap = new HashMap<Integer, List<String>> ();
        List<String> zero = new ArrayList<String>();
        zero.add("");
        dpMap.put(0, zero);

        return generateParenthesisDP(n);
    }
}
