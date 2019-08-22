class Solution {
    public String removeDuplicateLetters(String s) {
        if (s.length() < 2)
            return s;

        int[] numUniqueCharacters = new int[s.length()];
        Set<Character> uniqueChar = new HashSet<Character>();
        Set<Character> used = new HashSet<Character>();
        Map<Character, Integer> location = new HashMap<Character, Integer>();

        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            uniqueChar.add(c);
            numUniqueCharacters[i] = uniqueChar.size();
            if (!location.containsKey(c))
                location.put(c, i);
        }



        int ind = 0;
        int indChoice = 0;
        String ret = "";

        while (ret.length() < uniqueChar.size()) {
            char choice = 'z' + 1;
            while (ind < s.length() && numUniqueCharacters[ind] == uniqueChar.size() - used.size()) {
                if (s.charAt(ind) < choice && !used.contains(s.charAt(ind))) {
                    choice = s.charAt(ind);
                    indChoice = ind;
                }
                ind += 1;
            }

            for (int i = indChoice + 1; i <= location.get(s.charAt(indChoice)); i++)
                numUniqueCharacters[i] -= 1;

            used.add(choice);
            ret += choice;
            ind = indChoice + 1;
        }

        return ret;
    }
}
