class Solution {
    private Map<String, List<String>> combinations;

    private List<String> letterCombinationsDP(String digits) {
        if (combinations.containsKey(digits))
            return combinations.get(digits);

        List<String> lefts = letterCombinationsDP(digits.substring(0, 1));
        List<String> rights = letterCombinationsDP(digits.substring(1));

        List<String> ret = new ArrayList<String>();
        for (String left : lefts) {
            for (String right : rights)
                ret.add(left + right);
        }

        combinations.put(digits, ret);
        return ret;
    }

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0)
            return new ArrayList<String>();

        combinations = new HashMap<String, List<String>>();
        combinations.put("1", Arrays.asList("*"));
        combinations.put("0", Arrays.asList(" "));
        combinations.put("7", Arrays.asList("p", "q", "r", "s"));
        combinations.put("8", Arrays.asList("t", "u", "v"));
        combinations.put("9", Arrays.asList("w", "x", "y", "z"));

        for (int i = 0; i < 5; i++) {
            String key = "" + (i + 2);
            List<String> combinationsList = new ArrayList<String>();
            combinationsList.add("" + (char)(i * 3 + 'a'));
            combinationsList.add("" + (char)(i * 3 + 1 + 'a'));
            combinationsList.add("" + (char)(i * 3 + 2 + 'a'));
            combinations.put(key, combinationsList);
        }

        return letterCombinationsDP(digits);
    }
}
