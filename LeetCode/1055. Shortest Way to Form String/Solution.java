class Solution {
    public int shortestWay(String source, String target) {
        // space complexity: O(|source|)
        // time complexity: O(|source| + |target| log |source|)
        int[][] invertedIndex = new int[26][];
        for (int c = 0; c < 26; c++) {
            char character = (char) ('a' + c);
            List<Integer> inds = new ArrayList<Integer>();
            for (int i = 0; i < source.length(); i++) {
                if (source.charAt(i) == character)
                    inds.add(i);
            }
            invertedIndex[c] = new int[inds.size()];
            for (int i = 0; i < inds.size(); i++)
                invertedIndex[c][i] = inds.get(i);
        }

        int cur = 0;
        int ret = 0;
        int curLastInd = -1;

        while (cur < target.length()) {
            int charCode = (int) (target.charAt(cur) - 'a');
            if (invertedIndex[charCode].length == 0)
                return -1;

            if (curLastInd == -1) {
                curLastInd = invertedIndex[charCode][0];
                ret += 1;
                cur += 1;
            }
            else {
                int[] indices = invertedIndex[charCode];
                int ind = Arrays.binarySearch(indices, curLastInd + 1);
                if (ind < 0)
                    ind = -ind - 1;
                if (ind == indices.length)
                    curLastInd = -1;
                else {
                    curLastInd = indices[ind];
                    cur += 1;
                }
            }
        }

        return ret;
    }
}
