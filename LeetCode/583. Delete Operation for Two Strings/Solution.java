class Solution {
    int[][] LCS;

    public int max3(int a, int b, int c) {
        if (a >= b && a >= c)
            return a;
        else if (b >= c && b >= a)
            return b;

        return c;
    }

    public int LCSDP(String str1, String str2, int i, int j) {
        if (LCS[i][j] != -1)
            return LCS[i][j];

        int candidate1 = 0;
        if (str1.charAt(i) == str2.charAt(j))
            candidate1 = 1 + LCSDP(str1, str2, i - 1, j - 1);

        int candidate2 = LCSDP(str1, str2, i - 1, j);
        int candidate3 = LCSDP(str1, str2, i, j - 1);

        int ret = max3(candidate1, candidate2, candidate3);
        LCS[i][j] = ret;
        return ret;
    }
    public int minDistance(String word1, String word2) {
        int strLen1 = word1.length();
        int strLen2 = word2.length();

        if (strLen1 == 0 || strLen2 == 0)
            return strLen1 + strLen2;

        if (strLen1 == 1) {
            if (word2.indexOf(word1) != -1)
                return strLen2 - 1;
            else
                return strLen2 + 1;
        }

        if (strLen2 == 1) {
            if (word1.indexOf(word2) != -1)
                return strLen1 - 1;
            else
                return strLen1 + 1;
        }

        LCS = new int[strLen1][strLen2];
        for (int[] arr : LCS)
            Arrays.fill(arr, -1);

        boolean found = false;
        for (int i = 0; i < strLen1; i++) {
            if (word1.charAt(i) == word2.charAt(0))
                found = true;

            if (found)
                LCS[i][0] = 1;
            else
                LCS[i][0] = 0;
        }
        found = false;
        for (int j = 0; j < strLen2; j++) {
            if (word2.charAt(j) == word1.charAt(0))
                found = true;

            if (found)
                LCS[0][j] = 1;
            else
                LCS[0][j] = 0;
        }

        int common = LCSDP(word1, word2, strLen1 - 1, strLen2 - 1);
        return strLen1 + strLen2 - common * 2;

    }
}
