class PersistentTrie {
    private TrieNode root;

    public PersistentTrie() {
        root = new TrieNode();
    }

    public PersistentTrie(TrieNode root) {
        this.root = root;
    }

    public PersistentTrie insert(int[] digits) {
        return new PersistentTrie(insert(root, digits, 0));
    }

    private TrieNode insert(TrieNode node, int[] digits, int i) {
        TrieNode ret = new TrieNode();

        if (node != null) {
            ret.children[0] = node.children[0];
            ret.children[1] = node.children[1];
        }

        if (i < digits.length) {
            ret.children[digits[i]] = insert(ret.children[digits[i]], digits, i + 1);
        }

        return ret;
    }

    public int maxXor(int[] digits) {
        TrieNode it = root;
        int ret = 0;

        for (int digit : digits) {
            ret <<= 1;

            if (it.children[1 - digit] != null) {
                ret += 1;
                it = it.children[1 - digit];
            } else {
                it = it.children[digit];
            }
        }

        return ret;
    }

    class TrieNode {
        private TrieNode[] children;

        public TrieNode() {
            children = new TrieNode[2];
        }
    }

}


class Solution {
    private PersistentTrie[] trieInds;

    public int[] maxGeneticDifference(int[] parents, int[][] queries) {
        // Time Complexity: O((N + Q)W)
        // Space Complexity: O(NW)

        trieInds = new PersistentTrie[parents.length];
        int root = -1;

        int maxVal = parents.length - 1;
        for (int[] query : queries) {
            maxVal = Math.max(maxVal, query[1]);
        }

        int numDig = ((int) (Math.log10(maxVal) / Math.log10(2))) + 1;


        int[] ret = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            ret[i] = getTrie(query[0], parents, numDig).maxXor(toDigits(query[1], numDig));
        }

        return ret;
    }

    private PersistentTrie getTrie(int node, int[] parents, int numDig) {
        if (trieInds[node] != null)
            return trieInds[node];

        PersistentTrie ret;
        if (parents[node] == -1)
            ret = (new PersistentTrie()).insert(toDigits(node, numDig));
        else
            ret = (getTrie(parents[node], parents, numDig)).insert(toDigits(node, numDig));

        trieInds[node] = ret;
        return ret;
    }

    private int[] toDigits(int value, int numDig) {
        int[] ret = new int[numDig];

        int i = ret.length - 1;
        while (value > 0) {
            ret[i] = value & 1;
            value >>= 1;
            i -= 1;
        }

        return ret;
    }
}
