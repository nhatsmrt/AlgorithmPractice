class Solution {
    public int distinctEchoSubstrings(String text) {
        int[][] hashes = new int[text.length()][text.length()];

        for (int i = 0; i < text.length(); i++) {
            hashes[i][i] = (int) (text.charAt(i) - 'a');
            for (int j = i + 1; j < text.length(); j++)
                hashes[i][j] = hashes[i][j - 1] * 31 + (int) (text.charAt(j) - 'a');
        }

        Set<String> result = new HashSet<>();

        int ret = 0;
        for (int i = 0; i < text.length(); i++) {
            for (int j = 0; j < (text.length() - i) / 2; j++) {
                if (hashes[i][i + j] == hashes[i + j + 1][i + 2 * j + 1] &&
                    text.substring(i, i + j + 1).equals(text.substring(i + j + 1, i + 2 * j + 2)) &&
                    !result.contains(text.substring(i, i + j + 1))
                 )
                    result.add(text.substring(i, i + j + 1));
            }
        }
        return result.size();
    }
}
