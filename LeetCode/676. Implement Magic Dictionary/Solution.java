class MagicDictionary {
    private TrieNode root;

    /** Initialize your data structure here. */
    public MagicDictionary() {
        root = new TrieNode('$');
    }

    /** Build a dictionary through a list of words */
    public void buildDict(String[] dict) {
        for (String word : dict)
            add(root, word, 0);
    }

    public void add(TrieNode node, String word, int pos) {
        if (pos == word.length())
            node.isWord = true;
        else {
            char c = word.charAt(pos);
            if (!node.children.containsKey(c))
                node.children.put(c, new TrieNode(c));
            add(node.children.get(c), word, pos + 1);
        }
    }

    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    public boolean search(String word) {
        return search(root, word, 0, false);
    }

    private boolean search (TrieNode node, String word, int pos, boolean modified) {
        if (pos == word.length())
            return modified && node.isWord;

        char c = word.charAt(pos);
        if (node.children.containsKey(c)) {
            if (search(node.children.get(c), word, pos + 1, modified))
                return true;
            else if (modified)
                return false;
            else {
                for (TrieNode child : node.children.values()) {
                    if (child.c != c && search(child, word, pos + 1, true))
                        return true;
                }
            }
        }
        else {
            if (modified)
                return false;
            else {
                for (TrieNode child : node.children.values()) {
                    if (search(child, word, pos + 1, true))
                        return true;
                }
            }
        }

        return false;
    }

    private class TrieNode {
        char c;
        Map<Character, TrieNode> children;
        boolean isWord;

        public TrieNode(char c) {
            this.c = c;
            children = new HashMap<Character, TrieNode>();
            isWord = false;
        }
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * boolean param_2 = obj.search(word);
 */
