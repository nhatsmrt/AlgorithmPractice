class Solution {
    private int[] dp;

    public int longestStrChain(String[] words) {
        // Time Complexity: O(|W||V|^2)
        // Space Complexity: O(|V| + |E|)

        Map<Integer, Set<Integer>> adjLists = new HashMap<>();
        Map<Integer, Set<Integer>> byLength = new HashMap<>();

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (!byLength.containsKey(word.length()))
                byLength.put(word.length(), new HashSet<>());
            byLength.get(word.length()).add(i);
        }

        for (Integer len : byLength.keySet()) {
            if (byLength.containsKey(len + 1)) {
                Set<Integer> froms = byLength.get(len);
                Set<Integer> tos = byLength.get(len + 1);

                for (Integer from : froms) {
                    for (Integer to : tos) {
                        if (isAdjacent(words[from], words[to])) {
                            if (!adjLists.containsKey(from))
                                adjLists.put(from, new HashSet<>());
                            adjLists.get(from).add(to);
                        }
                    }
                }
            }
        }

        dp = new int[words.length];
        Arrays.fill(dp, -1);

        int ret = 0;
        for (int i = 0; i < words.length; i++) {
            int candidate = longestStrChain(adjLists, i);
            if (candidate > ret)
                ret = candidate;
        }

        return ret;
    }

    private int longestStrChain(Map<Integer, Set<Integer>> adjLists, int i) {
        if (dp[i] != -1)
            return dp[i];

        int ret = 1;
        if (adjLists.containsKey(i)) {
            Set<Integer> neighbors = adjLists.get(i);

            for (Integer j : neighbors) {
                int candidate = longestStrChain(adjLists, j) + 1;
                if (ret < candidate)
                    ret = candidate;
            }
        }

        dp[i] = ret;
        return ret;
    }

    private boolean isAdjacent(String word1, String word2) {
        if (word1.length() + 1 != word2.length())
            return false;

        int it2 = 0;

        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) == word2.charAt(it2))
                it2 += 1;
            else {
                if (it2 == i && word2.charAt(it2 + 1) == word1.charAt(i))
                    it2 += 1;
                else
                    return false;
            }
        }

        return true;
    }
}
