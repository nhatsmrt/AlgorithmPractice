class Solution {
    private Set<Character> start;

    public boolean isSolvable(String[] words, String result) {
        Set<Character> allChars = new HashSet<>();
        start = new HashSet<>();

        for (String word : words) {
            start.add(word.charAt(0));
            for (int i = 0; i < word.length(); i++) {
                allChars.add(word.charAt(i));
            }
        }
        start.add(result.charAt(0));
        for (int i = 0; i < result.length(); i++)
            allChars.add(result.charAt(i));

        List<Character> charList = new ArrayList<>(allChars);

        int[] map = new int[26];
        char[] reverse = new char[10];
        Arrays.fill(reverse, '$');
        Arrays.fill(map, -1);


        return backtrack(words, result, charList, 0, map, reverse);
    }


    private boolean backtrack(
        String[] words, String result, List<Character> charList, int ind, int[] map, char[] reverse
    ) {

        if (ind == charList.size()) {
            return checkLegit(words, result, map);
        }

        Character next = charList.get(ind);

        for (int i = 0; i < 10; i++) {
            if (reverse[i] == '$' && !(i == 0 && start.contains(next))) {
                // choose
                map[(int) (next - 'A')] = i;
                reverse[i] = next;
                // check
                if (backtrack(words, result, charList, ind + 1, map, reverse))
                    return true;
                // unchoose
                map[(int) (next - 'A')] = -1;
                reverse[i] = '$';
            }
        }

        return false;
    }


    private boolean checkLegit(String[] words, String result, int[] map) {
        int resultVal = decode(result, map);

        int lhs = 0;
        for (String word : words) {
            lhs += decode(word, map);
            if (lhs > resultVal)
                return false;
        }
        return lhs == resultVal;
    }

    private int decode(String word, int[] map) {
        int ret = 0;
        for (int i = 0; i < word.length(); i++) {
            ret = ret * 10 + map[(int) (word.charAt(i) - 'A')];
        }

        return ret;
    }
}
