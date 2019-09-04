public class Trie {
    TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        Map<Character, TrieNode> children = root.children;
        TrieNode t;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (children.containsKey(c))
                t = children.get(c);
            else {
                t = new TrieNode(c);
                children.put(c, t);
            }

            children = t.children;

            // Leaf:
            if (i == word.length() - 1)
                t.isLeaf = true;
        }
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode t = searchNode(word);
        if (t != null && t.isLeaf)
            return true;
        else
            return false;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode t = searchNode(prefix);
        if (t != null)
            return true;
        else
            return false;
    }

    // Return the node corresponding to the final character of the word (if found)
    // or null
    private TrieNode searchNode(String word) {
        Map<Character, TrieNode> children = root.children;
        TrieNode t = null;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            if (children.containsKey(c)) {
                t = children.get(c);
                children = t.children;
            }
            else
                return null;

        }

        return t;
    }

    private class TrieNode {
        public char c;
        public Map<Character, TrieNode> children;
        public boolean isLeaf;

        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
        }

        public TrieNode(char c) {
            this.c = c;
            children = new HashMap<Character, TrieNode>();
        }

        public void addNext(TrieNode newNext) {
            children.put(newNext.c, newNext);
        }
    }
}
