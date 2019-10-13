class Graph {
    private Map<Character, Set<Character>> adjLists;
    private Map<Character, Integer> indegree;

    public Graph() {
        adjLists = new HashMap<Character, Set<Character>>();
        indegree = new HashMap<Character, Integer>();
    }

    public void addNode(char c) {
        if (!adjLists.containsKey(c)) {
            // new node
            adjLists.put(c, new HashSet<Character>());
            indegree.put(c, 0);
        }
    }

    public void addEdge(char c1, char c2) {
        if (adjLists.get(c1).add(c2)) {
            // new edge
            int indeg = indegree.get(c2);
            indegree.put(c2, indeg + 1);
        }
    }

    public String topologicalSort() {
        // Kahn's algorithm

        Queue<Character> traverse = new LinkedList<Character>();
        for (Character node : adjLists.keySet()) {
            if (indegree.get(node) == 0)
                traverse.add(node);
        }
        if (traverse.isEmpty())
            return "";

        StringBuilder ret = new StringBuilder();
        while (!traverse.isEmpty()) {
            char node = traverse.remove();
            ret.append(node);
            for (char child : adjLists.get(node)) {
                int indeg = indegree.get(child);

                if (indeg == 1)
                    traverse.add(child);
                else
                    indegree.put(child, indeg - 1);
            }
        }

        if (ret.length() == adjLists.keySet().size())
            return ret.toString();
        return "";
    }
}


class Solution {
    public String alienOrder(String[] words) {
        Graph g = new Graph();

        for (String word : words) {
            for (int i = 0; i < word.length(); i++)
                g.addNode(word.charAt(i));
        }

        for (int m = 1; m < words.length; m++) {
                String word1 = words[m - 1];
                String word2 = words[m];

                int j = 0;
                while (j < word1.length() && j < word2.length() && word1.charAt(j) == word2.charAt(j))
                    j += 1;

                if (j < word1.length() && j < word2.length())
                    g.addEdge(word1.charAt(j), word2.charAt(j));
        }

        return g.topologicalSort();
    }
}
