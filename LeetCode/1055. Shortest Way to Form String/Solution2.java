class Solution {
    public int shortestWay(String source, String target) {
        // space complexity: O(|source|)
        // time complexity: O(|source| + |target|)
        int[][] suffInvertedIndex = new int[source.length() + 1][26];
        for (int[] subarr : suffInvertedIndex)
            Arrays.fill(subarr, - 1);

        for (int i = source.length() - 1; i >= 0; i--) {
            for (int j = 0; j < 26; j++)
                suffInvertedIndex[i][j] = suffInvertedIndex[i + 1][j];
            int charCode = (int) (source.charAt(i) - 'a');
            suffInvertedIndex[i][charCode] = i;
        }

        int cur = 0;
        int ret = 1;
        int suffInd = 0;

        while (cur < target.length()) {
            int charCode = (int) (target.charAt(cur) - 'a');

            if (suffInvertedIndex[suffInd][charCode] == -1) {
                if (suffInd == 0)
                    return -1;
                suffInd = 0;
                ret += 1;
            }
            else {
                suffInd = suffInvertedIndex[suffInd][charCode] + 1;
                cur++;
            }
        }

        return ret;
    }
}
