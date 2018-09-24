class Solution {
    int[][] LevDist;
    public int min3(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= c && b <= a)
            return b;

        return c;
    }
    public int LevDistDP(String str1, String str2, int i, int j) {
        if (LevDist[i][j] != -1)
            return LevDist[i][j];

        int candidate1 = LevDistDP(str1, str2, i - 1, j - 1);
        if (str1.charAt(i - 1) != str2.charAt(j - 1))
            candidate1 += 1;

        int candidate2 = LevDistDP(str1, str2, i - 1, j) + 1;
        int candidate3 = LevDistDP(str1, str2, i, j - 1) + 1;

        int ret = min3(candidate1, candidate2, candidate3);
        LevDist[i][j] = ret;

        return ret;
    }

    public int minDistance(String word1, String word2) {
        int strLen1 = word1.length();
        int strLen2 = word2.length();

        if (strLen1 == 0 || strLen2 == 0)
            return strLen1 + strLen2;

        LevDist = new int[strLen1 + 1][strLen2 + 1];
        for (int[] arr : LevDist)
            Arrays.fill(arr, -1);

        for (int i = 0; i <= strLen1; i++) {
            LevDist[i][0] = i;
        }

        for (int j = 0; j <= strLen2; j++) {
            LevDist[0][j] = j;
        }

        return LevDistDP(word1, word2, strLen1, strLen2);
    }
}
