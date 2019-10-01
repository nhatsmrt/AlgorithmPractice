class Solution {
    public String lastSubstring(String s) {
        s = s + (char) ('a' - 1);

        List<Suffix> suffixArray = new ArrayList<Suffix>();
        for (int i = 0; i < s.length(); i++) {
            Suffix suf = new Suffix(s, i);
            suffixArray.add(suf);
        }

        int length = 2;
        int rank = 27;
        while (length <= s.length()) {
            rank = radixSort(suffixArray, length, rank);
            if (
                suffixArray.get(suffixArray.size() - 1).rank[0] !=
                suffixArray.get(suffixArray.size() - 2).rank[0]
            )
                break;
            length *= 2;
        }

        if (
            suffixArray.get(suffixArray.size() - 1).rank[0] ==
            suffixArray.get(suffixArray.size() - 2).rank[0]
        )
            radixSort(suffixArray, length, rank);

        return s.substring(
            suffixArray.get(suffixArray.size() - 1).ind,
            s.length() - 1
        );
    }

    private class Suffix {
        int ind;
        int[] rank;
        String s;

        public Suffix(String s, int ind) {
            this.ind = ind;
            this.s = s;
            rank = new int[2];

            rank[0] = s.charAt(ind) - '`';
            rank[1] = s.charAt((ind + 1) % s.length()) - '`';
        }

        public String toString() {
            return s.substring(ind);
        }
    }

    public int radixSort(List<Suffix> suffixArray, int length, int oldRank) {
        radixSortIter(suffixArray, 1, oldRank);
        radixSortIter(suffixArray, 0, oldRank);

        int rank = 0;
        int cur = 0;
        int[] newRank2 = new int[suffixArray.size()];
        Suffix suf = suffixArray.get(0);
        suf.rank[0] = 0;

        for (int i = 1; i < suffixArray.size(); i++) {
            Suffix nextSuf = suffixArray.get(i);
            if (nextSuf.rank[0] > suf.rank[0] || nextSuf.rank[1] > suf.rank[1]) {
                rank += 1;
                suf = nextSuf;
            }
            newRank2[suffixArray.get(i).ind] = rank;
        }


        for (int i = 0; i < suffixArray.size(); i++) {
            int ind = suffixArray.get(i).ind;

            suffixArray.get(i).rank[0] = newRank2[ind];
            suffixArray.get(i).rank[1] = newRank2[(ind + length) % suffixArray.size()];
        }

        return rank;
    }

    private void radixSortIter(List<Suffix> suffixArray, int pos, int rank) {

        List<List<Suffix>> count = new ArrayList<List<Suffix>>();
        for (int i = 0; i < rank + 1; i++)
            count.add(new ArrayList<Suffix>());

        for (Suffix suf : suffixArray) {
            count.get(suf.rank[pos]).add(suf);
        }

        int cur = 0;
        for (List<Suffix> list : count) {
            for (Suffix suf : list) {
                suffixArray.set(cur, suf);
                cur += 1;
            }
        }
    }
}
