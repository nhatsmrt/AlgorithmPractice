class AutocompleteSystem {
    private StringBuilder cur;
    private TrieNode root;
    private TrieNode curNode;

    public AutocompleteSystem(String[] sentences, int[] times) {
        cur = new StringBuilder();
        root = new TrieNode();
        curNode = root;

        for (int i = 0; i < sentences.length; i++)
            add(sentences[i], times[i]);
    }

    public List<String> input(char c) {
        List<String> ret = new ArrayList<String>();
        if (c == '#') {
            if (!curNode.isWord) {
                curNode.isWord = true;
                curNode.word = cur.toString();
            }
            curNode.freq += 1;
            cur = new StringBuilder();
            curNode = root;
        }
        else {
            cur.append(c);
            if (!curNode.children.containsKey(c))
                curNode.children.put(c, new TrieNode(c));
            curNode = curNode.children.get(c);
            List<TrieNode> allWords = new ArrayList<TrieNode>();
            findWords(curNode, allWords);
            PriorityQueue<TrieNode> queue = new PriorityQueue<TrieNode>(allWords);
            for (int i = 0; i < 3; i++) {
                if (queue.isEmpty())
                    break;
                ret.add(queue.poll().word);
            }
        }

        return ret;
    }

    private void findWords(TrieNode node, List<TrieNode> ret) {
        if (node.isWord)
            ret.add(node);
        for (TrieNode child : node.children.values())
            findWords(child, ret);
    }

    private void add(String word, int freq) {
        TrieNode it = root;
        for (int i = 0; i < word.length(); i++) {
            if (!it.children.containsKey(word.charAt(i)))
                it.children.put(word.charAt(i), new TrieNode(word.charAt(i)));
            it = it.children.get(word.charAt(i));
        }
        if (!it.isWord)
            it.isWord = true;
        it.word = word;
        it.freq += freq;
    }

    private class TrieNode implements Comparable<TrieNode> {
        char c;
        Map<Character, TrieNode> children;
        boolean isWord;
        String word;
        int freq;

        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
        }

        public TrieNode(char c) {
            children = new HashMap<Character, TrieNode>();
            this.c = c;
        }

        public int compareTo(TrieNode other) {
            if (freq != other.freq)
                return Integer.compare(other.freq, freq);

            return word.compareTo(other.word);
        }
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */
