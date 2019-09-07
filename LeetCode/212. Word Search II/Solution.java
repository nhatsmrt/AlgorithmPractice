class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }


    public void add(String str) {
        TrieNode node = root;
        for (int i = 0; i < str.length(); i++) {
            if (!node.children.containsKey(str.charAt(i)))
                node.children.put(str.charAt(i), new TrieNode(str.charAt(i)));

            node = node.children.get(str.charAt(i));
        }

        node.isWord = true;
    }


    public boolean search(StringBuilder str) {
        TrieNode node = root;
        for (int i = 0; i < str.length(); i++) {
            if (!node.children.containsKey(str.charAt(i)))
                return false;
            node = node.children.get(str.charAt(i));
        }

        return node.isWord;
    }


    public boolean isPrefix(StringBuilder str) {
        TrieNode node = root;
        for (int i = 0; i < str.length(); i++) {
            if (!node.children.containsKey(str.charAt(i)))
                return false;
            node = node.children.get(str.charAt(i));
        }

        return true;
    }


    private class TrieNode {
        Map<Character, TrieNode> children;
        Character c;
        boolean isWord;

        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
            isWord = false;
        }

        public TrieNode(Character c) {
            this.c = c;
            children = new HashMap<Character, TrieNode>();
            isWord = false;
        }
    }
}


class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Trie trie = new Trie();
        Set<String> wordSet = new HashSet<String>();

        for (String word : words) {
            trie.add(word);
            wordSet.add(word);
        }

        Set<String> solution = new HashSet<String>();
        boolean[][] status = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                StringBuilder str = new StringBuilder();
                str.append(board[i][j]);
                if (trie.isPrefix(str)) {
                    search(board, status, i, j, solution, str, trie, wordSet);
                }
            }
        }

        List<String> ret = new ArrayList<String>();
        for (String str : solution)
            ret.add(str);

        return ret;
    }


    private void search(
        char[][] board, boolean[][] status, int i, int j,
        Set<String> solution, StringBuilder curStr, Trie trie, Set<String> wordSet
    ) {
        status[i][j] = true;
        if (wordSet.contains(curStr.toString()))
            solution.add(curStr.toString());

        if (i > 0 && !status[i - 1][j]) {
            curStr.append(board[i - 1][j]);
            if (trie.isPrefix(curStr))
                search(board, status, i - 1, j, solution, curStr, trie, wordSet);

            curStr.deleteCharAt(curStr.length() - 1);
        }

        if (i < board.length - 1 && !status[i + 1][j]) {
            curStr.append(board[i + 1][j]);
            if (trie.isPrefix(curStr))
                search(board, status, i + 1, j, solution, curStr, trie, wordSet);

            curStr.deleteCharAt(curStr.length() - 1);
        }

        if (j > 0 && !status[i][j - 1]) {
            curStr.append(board[i][j - 1]);
            if (trie.isPrefix(curStr))
                search(board, status, i, j - 1, solution, curStr, trie, wordSet);

            curStr.deleteCharAt(curStr.length() - 1);
        }


        if (j < board[0].length - 1 && !status[i][j + 1]) {
            curStr.append(board[i][j + 1]);
            if (trie.isPrefix(curStr))
                search(board, status, i, j + 1, solution, curStr, trie, wordSet);

            curStr.deleteCharAt(curStr.length() - 1);
        }


        status[i][j] = false;
    }
}
