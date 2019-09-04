class WordDictionary {
    private TrieNode root;

    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
        if (word.length() > 0) {
            TrieNode node = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                if (!node.children.containsKey(c))
                    node.children.put(c, new TrieNode(c));
                node = node.children.get(c);
            }
            node.isWord = true;
        }
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return searchSuffix(word, 0, root);
    }

    private boolean searchSuffix(String word, int ind, TrieNode node) {
        if (ind == word.length())
            return node.isWord;
        else {
            if (word.charAt(ind) == '.') {
                for (Character c : node.children.keySet()) {
                    if (searchSuffix(word, ind + 1, node.children.get(c)))
                        return true;
                }
                return false;
            }
            else {
                if (node.children.containsKey(word.charAt(ind)))
                    return searchSuffix(word, ind + 1, node.children.get(word.charAt(ind)));
                else
                    return false;
            }
        }
    }

    private class TrieNode {
        public Character character;
        public Map<Character, TrieNode> children;
        public boolean isWord;

        public TrieNode() {
            isWord = false;
            children = new HashMap<Character, TrieNode>();
        }

        public TrieNode(Character c) {
            isWord = false;
            children = new HashMap<Character, TrieNode>();
            character = c;
        }
    }
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
