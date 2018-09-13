// Based on https://www.programcreek.com/2014/05/leetcode-implement-trie-prefix-tree-java/
class Trie {
    TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        HashMap<Character, TrieNode> children = root.getChildren();
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
                t.setLeaf(true);
        }
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode t = searchNode(word);
        if (t != null && t.getLeaf())
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
        HashMap<Character, TrieNode> children = root.getChildren();
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

    class TrieNode {
        private char c;
        private HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
        private boolean isLeaf;

        public TrieNode() {
        }

        public TrieNode(char c) {
            this.c = c;
        }

        public char getChar() {
            return c;
        }

        public boolean getLeaf() {
            return isLeaf;
        }

        public HashMap<Character, TrieNode> getChildren() {
            return children;
        }

        public void setChar(char newChar) {
            c = newChar;
        }

        public void addNext(TrieNode newNext) {
            children.put(newNext.getChar(), newNext);
        }

        public void setLeaf(boolean isLeaf) {
            this.isLeaf = isLeaf;
        }
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
