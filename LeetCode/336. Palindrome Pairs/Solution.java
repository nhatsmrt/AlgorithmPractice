class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void add(String word, int ind) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            if (!node.children.containsKey(word.charAt(i)))
                node.children.put(word.charAt(i), new TrieNode(word.charAt(i)));
            node = node.children.get(word.charAt(i));
        }
        node.ind = ind;
    }

    public List<Integer> findPairs(String word) {
        List<Integer> ret = new ArrayList<Integer>();
        TrieNode node = root;

        StringBuilder cur = new StringBuilder(word);
        for (int i = word.length() - 1; i >= 0; i--) {
            if (!node.children.containsKey(word.charAt(i)))
                return ret;
            node = node.children.get(word.charAt(i));
            cur.deleteCharAt(cur.length() - 1);
            if (node.ind != -1 && isPalindrome(cur))
                ret.add(node.ind);
        }

        for (TrieNode child : node.children.values()) {
            findPalindromeFrom(cur, child, ret);
        }

        return ret;
    }

    public void findPalindromeFrom(StringBuilder cur, TrieNode node, List<Integer> ret) {
        cur.append(node.value);
        if (node.ind != -1 && isPalindrome(cur))
            ret.add(node.ind);

        for (TrieNode child : node.children.values()) {
            findPalindromeFrom(cur, child, ret);
        }
        cur.deleteCharAt(cur.length() - 1);
    }

    private boolean isPalindrome(StringBuilder word) {
        if (word.length() < 2)
            return true;

        for (int i = 0; i < word.length() / 2; i++) {
            if (word.charAt(i) != word.charAt(word.length() - 1 - i))
                return false;
        }

        return true;
    }

    private class TrieNode {
        char value;
        Map<Character, TrieNode> children;
        int ind;

        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
            ind = -1;
        }

        public TrieNode(char value) {
            this.value = value;
            children = new HashMap<Character, TrieNode>();
            ind = -1;
        }
    }
}


class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            if (words[i].length() > 0)
                trie.add(words[i], i);
        }

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].length() == 0) {
                for (int j = 0; j < words.length; j++) {
                    if ((words[j].length() > 0 && isPalindrome(words[j])) || (words[j].length() == 0 && j > i)) {
                        List<Integer> pair = new ArrayList<Integer>();
                        pair.add(i);
                        pair.add(j);
                        ret.add(pair);

                        pair = new ArrayList<Integer>();
                        pair.add(j);
                        pair.add(i);
                        ret.add(pair);
                    }
                }
            }
            else {
                List<Integer> palindromePairs = trie.findPairs(words[i]);
                for (Integer ind : palindromePairs) {
                    if (ind != i) {
                        List<Integer> pair = new ArrayList<Integer>();
                        pair.add(ind);
                        pair.add(i);
                        ret.add(pair);
                    }
                }
            }
        }

        return ret;
    }

    private boolean isPalindrome(String word) {
        if (word.length() < 2)
            return true;

        for (int i = 0; i < word.length() / 2; i++) {
            if (word.charAt(i) != word.charAt(word.length() - 1 - i))
                return false;
        }

        return true;
    }
}
