/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */
class Solution {
    public void findSecretWord(String[] wordlist, Master master) {
        Map<String, Map<Integer, Set<String>>> map = new HashMap<String, Map<Integer, Set<String>>>();
        for (String word : wordlist)
            map.put(word, new HashMap<Integer, Set<String>>());

        Map<String, Integer> maxMap = new HashMap<String, Integer>();
        Set<String> candidates = new HashSet<String>();

        for (int i = 0; i < wordlist.length; i++) {
            String first = wordlist[i];
            for (int j = i + 1; j < wordlist.length; j++) {
                String second = wordlist[j];

                int diff = computeDiff(first, second);
                Map<Integer, Set<String>> diffMap = map.get(first);
                if (!diffMap.containsKey(diff))
                    diffMap.put(diff, new HashSet<String>());
                diffMap.get(diff).add(second);

                diffMap = map.get(second);
                if (!diffMap.containsKey(diff))
                    diffMap.put(diff, new HashSet<String>());
                diffMap.get(diff).add(first);
            }
            int maxSize = 0;
            for (Integer diff : map.get(first).keySet()) {
                int candidateSize = map.get(first).get(diff).size();
                if (candidateSize > maxSize)
                    maxSize = candidateSize;
            }
            maxMap.put(first, maxSize);
            candidates.add(first);
        }

        String candidate = next(candidates, maxMap);
        int diff = master.guess(wordlist[0]);
        
        if (diff != 6) {
            candidates = map.get(wordlist[0]).get(diff);

            while (diff != 6) {
                String nextCandidate = next(candidates, maxMap);
                diff = master.guess(nextCandidate);
                if (map.get(nextCandidate).get(diff) != null)
                    candidates.retainAll(map.get(nextCandidate).get(diff));
            }
        }
    }

    private String next(Set<String> candidates, Map<String, Integer> maxMap) {
        String ret = "";
        int min = -1;
        Iterator<String> it = candidates.iterator();
        while (it.hasNext()) {
            String candidate = it.next();
            int score = maxMap.get(candidate);
            if (min == -1 || min > score) {
                min = score;
                ret = candidate;
            }
        }

        candidates.remove(ret);
        return ret;
    }

    private int computeDiff(String first, String second) {
        int diff = 0;
        for (int i = 0; i < 6; i++) {
            if (first.charAt(i) == second.charAt(i))
                diff += 1;
        }

        return diff;
    }
}
