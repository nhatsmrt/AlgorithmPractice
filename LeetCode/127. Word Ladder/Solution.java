class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        boolean adjListContainsEnd = false;
        Map<String, Set<String>> adjLists = new HashMap<String, Set<String>>();

        adjLists.put(beginWord, new HashSet<String>());
        adjLists.put(endWord, new HashSet<String>());
        for (int i = 0; i < wordList.size(); i++) {
            adjLists.put(wordList.get(i), new HashSet<String>());
            adjListContainsEnd = adjListContainsEnd || wordList.get(i).equals(endWord);
        }


        if (!adjListContainsEnd)
            return 0;

        if (isAdjacent(beginWord, endWord))
            return 2;


        for (int i = 0; i < wordList.size(); i++) {
            for (int j = i + 1; j < wordList.size(); j++) {
                if (isAdjacent(wordList.get(i), wordList.get(j))) {
                    adjLists.get(wordList.get(i)).add(wordList.get(j));
                    adjLists.get(wordList.get(j)).add(wordList.get(i));
                }
            }

            if (isAdjacent(beginWord, wordList.get(i)) && !beginWord.equals(wordList.get(i))) {
                adjLists.get(wordList.get(i)).add(beginWord);
                adjLists.get(beginWord).add(wordList.get(i));
            }


        }

        Queue<String> traverseQueue = new LinkedList<String>();
        traverseQueue.add(beginWord);
        Set<String> visited = new HashSet<String>();

        int level = 0;
        int nodeInCurLevel = 1;
        while (!traverseQueue.isEmpty()) {
            System.out.println(traverseQueue);
            System.out.println(level);
            String cur = traverseQueue.remove();

            if (cur.equals(endWord))
                return level + 1;

            nodeInCurLevel -= 1;

            for (String neighbor : adjLists.get(cur)) {
                if (!visited.contains(neighbor))
                    traverseQueue.add(neighbor);
                visited.add(neighbor);
            }

            if (nodeInCurLevel == 0) {
                level += 1;
                nodeInCurLevel = traverseQueue.size();
            }
        }



        return 0;

    }

    private boolean isAdjacent(String str1, String str2) {
        int numDiff = 0;
        int i = 0;

        while (i < str1.length() && numDiff < 2) {
            if (str1.charAt(i) != str2.charAt(i))
                numDiff += 1;

            i += 1;
        }

        return numDiff < 2;
    }
}
