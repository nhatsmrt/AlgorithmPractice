class Solution {
    public boolean backspaceCompare(String S, String T) {
        List<Character> str1 = build(S);
        List<Character> str2 = build(T);

        if (str1.size() != str2.size())
            return false;

        for (int i = 0; i < str1.size(); i++) {
            if (str1.get(i) != str2.get(i))
                return false;
        }

        return true;
    }

    private List<Character> build (String s) {
        List<Character> ret = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '#') {
                if (ret.size() > 0)
                    ret.remove(ret.size() - 1);
            }
            else
                ret.add(s.charAt(i));
        }

        return ret;
    }
}
