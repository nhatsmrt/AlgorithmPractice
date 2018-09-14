public class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        String[] words = s.split("[ ]+");
        String ret = "";

        for (int i = words.length - 1; i >= 0; i--) {
            ret = ret + words[i];
            if (i != 0)
                ret = ret + " ";
        }

        return ret;
    }
}
