class Data {
    List<String> parents;
    int level;
    String value;

    public Data(String value, int level) {
        parents = new ArrayList<String>();
        this.level = level;
        this.value = value;
    }
}


class Solution {
    public List<List<String>> findLadders(
        String beginWord, String endWord, List<String> wordList
    ) {
        List<List<String>> ret = new ArrayList<List<String>>();
        Map<String, Set<String>> adjMap = new HashMap<String, Set<String>>();
        Set<String> changeableFromBegin = new HashSet<String>();
        for (String word : wordList)
            adjMap.put(word, new HashSet<String>());

        for (int i = 0; i < wordList.size(); i++) {
            for (int j = i + 1; j < wordList.size(); j++) {
                if (changeable(wordList.get(i), wordList.get(j))) {
                    adjMap.get(wordList.get(i)).add(wordList.get(j));
                    adjMap.get(wordList.get(j)).add(wordList.get(i));
                }
            }

            if (changeable(beginWord, wordList.get(i)))
                changeableFromBegin.add(wordList.get(i));
        }

        if (!adjMap.containsKey(endWord))
            return ret;

        if (changeable(beginWord, endWord)) {
            List<String> entry = new ArrayList<String>();
            entry.add(beginWord);
            entry.add(endWord);
            ret.add(entry);
            return ret;
        }

        Queue<String> traverse = new LinkedList<String>();
        Map<String, Data> data = new HashMap<String, Data>();
        data.put(endWord, new Data(endWord, 1));
        traverse.add(endWord);
        int curLevel = 1;

        while (!traverse.isEmpty()) {
            String word = traverse.remove();
            int level = data.get(word).level;
            for (String neighbor : adjMap.get(word)) {
                if (!data.containsKey(neighbor)) {
                    Data item = new Data(neighbor, level + 1);
                    item.parents.add(word);
                    data.put(neighbor, item);
                    traverse.add(neighbor);
                }
                else {
                    Data item = data.get(neighbor);
                    if (item.level == level + 1) {
                        item.parents.add(word);
                    }
                }
            }
        }

        int best = -1;
        for (String word : changeableFromBegin) {
            if (data.containsKey(word) && (best == -1 || data.get(word).level < best))
                best = data.get(word).level;
        }

        if (best == -1)
            return ret;

        for (String word : changeableFromBegin) {
            if (data.containsKey(word) && data.get(word).level == best) {
                List<String> partialSol = new ArrayList<String>();
                partialSol.add(beginWord);
                partialSol.add(word);
                buildSolution(data, data.get(word), partialSol, ret);
            }
        }

        return ret;
    }

    private void buildSolution(
        Map<String, Data> dataMap, Data item,
        List<String> partialSol, List<List<String>> ret
    ) {
        if(item.parents.size() == 0)
            ret.add(new ArrayList(partialSol));
        else {
            for (String parent : item.parents) {
                partialSol.add(parent);
                buildSolution(dataMap, dataMap.get(parent), partialSol, ret);
                partialSol.remove(parent);
            }
        }
    }

    private boolean changeable(String word1, String word2) {
        boolean found = false;

        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                if (found)
                    return false;
                else
                    found = true;
            }
        }

        return true;
    }
}
