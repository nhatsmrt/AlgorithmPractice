class Solution {
    public String toLowerCase(String str) {
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) <= 'Z' && str.charAt(i) >= 'A')
                ret.append((char) (str.charAt(i) - 'A' + 'a'));
            else
                ret.append(str.charAt(i));
        }

        return ret.toString();
    }
}
