class Solution {
    public String reverseVowels(String s) {
        List<Character> vowels = new ArrayList<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i)))
                vowels.add(s.charAt(i));
        }
        if (vowels.size() <= 1)
            return s;

        StringBuilder builder = new StringBuilder();
        int tmp = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) {
                builder.append(vowels.get(vowels.size() - 1 - tmp));
                tmp += 1;
            }
            else
                builder.append(s.charAt(i));
        }

        return builder.toString();

    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
