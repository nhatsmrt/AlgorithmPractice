class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Trie trie = new Trie();
        List<String> ret = new ArrayList<>();


        for (int i = 0; i < words.length; i++) {
            if (words[i].length() > 0)
                trie.add(words[i], i);
        }

        for (String word : words) {
            if (trie.isConcatenated(word))
                ret.add(word);
        }

        return ret;
    }

    private class Trie {
        TrieNode root;

        public Trie() {
            root = new TrieNode('$');
        }

        public void add(String word, int ind) {
            TrieNode it = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);
                int charInd = (int) c - (int) 'a';
                if (it.children[charInd] == null)
                    it.children[charInd] = new TrieNode(c);

                it = it.children[charInd];
            }

            it.ind = ind;
        }

        public boolean isConcatenated(String word) {
            return isConcatenated(word, root, 0, false);
        }

        public boolean isConcatenated(String word, TrieNode node, int i, boolean seen) {
            if (i == word.length()) {
                if (node.ind == -1)
                    return false;
                else {
                    return seen;
                }
            }

            boolean ret = false;

            if (node.ind != -1)
                ret = isConcatenated(word, root, i, true);

            if (ret)
                return true;
            else {
                int charInd = (int) word.charAt(i) - (int) 'a';
                if (node.children[charInd] == null)
                    return false;
                else
                    return isConcatenated(word, node.children[charInd], i + 1, seen);
            }

        }

        private class TrieNode {
            public int ind;
            public char c;
            public TrieNode[] children;

            public TrieNode(char c) {
                this.c = c;
                ind = -1;
                children = new TrieNode[26];
            }
        }
    }
}
