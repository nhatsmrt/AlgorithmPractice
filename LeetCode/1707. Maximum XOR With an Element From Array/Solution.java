class Solution {
    public int[] maximizeXor(int[] nums, int[][] queries) {
        // Time Complexity: O((N + Q) W)
        // Space Complexity: O(NW)
        // where W = log_2(MAX) <= 30

        Trie trie = new Trie(getDigits(1000000000, -1).size());

        for (int num : nums)
            trie.insert(num);

        int[] ret = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int value = queries[i][0];
            int boundary = queries[i][1];

            int answer = trie.query(value, boundary);

            if (answer >= 0)
                ret[i] = answer ^ value;
            else
                ret[i] = -1;
        }

        return ret;
    }

    private class Trie {
        int pad;
        TrieNode root;

        public Trie(int pad) {
            this.pad = pad;
            root = new TrieNode();
        }

        public void insert(int num) {
            List<Integer> digits = getDigits(num, pad);
            TrieNode it = root;

            for (int digit : digits) {
                it.min = Math.min(it.min, num);

                if (it.children[digit] == null)
                    it.children[digit] = new TrieNode();

                it = it.children[digit];
            }

            it.min = Math.min(it.min, num);
        }

        public int query(int value, int boundary) {
            if (root.min > boundary)
                return -1;

            List<Integer> valueDigits = getDigits(value, pad);
            List<Integer> retDigits = new ArrayList<>();
            TrieNode it = root;

            for (int valueDig : valueDigits) {
                int preferred = 1 - valueDig;
                int choice = it.children[preferred] != null && it.children[preferred].min <= boundary ? preferred : 1 - preferred;

                retDigits.add(choice);
                it = it.children[choice];
            }

            return toNum(retDigits);
        }

        private class TrieNode {
            int min;
            TrieNode[] children;

            public TrieNode() {
                children = new TrieNode[2];
                min = 1000000007;
            }
        }
    }

    private List<Integer> getDigits(int num, int pad) {
        List<Integer> digits = new ArrayList<Integer>();

        if (num == 0) {
            digits.add(0);
        } else {
            if (pad > 0) {
                for (int i = 0; i < pad; i++) {
                    if (num == 0)
                        break;
                    else {
                        digits.add(num & 1);
                        num >>= 1;
                    }
                }
            } else {
                while (num > 0) {
                    digits.add(num & 1);
                    num >>= 1;
                }
            }
        }

        if (pad > 0) {
            while (digits.size() < pad)
                digits.add(0);
        }

        Collections.reverse(digits);
        return digits;
    }

    private int toNum(List<Integer> digits) {
        int ret = 0;
        for (int dig : digits)
            ret = ret * 2 + dig;

        return ret;
    }
}
