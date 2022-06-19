import java.util.SortedMap;

class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        // Time Complexity: O(N log N)
        // each point is added and remove to frontier O(1) times
        // and each operation takes O(log N) work
        // Space Complexity: O(N)

        SortedMap<Integer, SortedMap<Integer, Integer>> frontier = new TreeMap<>();
        int ret = 0;

        for (int[] property : properties) {
            int att = property[0];
            int def = property[1];

            SortedMap<Integer, SortedMap<Integer, Integer>> tail = frontier.tailMap(att + 1);

            if (tail.isEmpty() || tail.get(tail.firstKey()).lastKey() <= def) {
                SortedMap<Integer, SortedMap<Integer, Integer>> head = frontier.headMap(att);

                while (!head.isEmpty()) {
                    int cand = head.lastKey();

                    if (head.get(cand).isEmpty()) {
                        frontier.remove(cand);
                        head = frontier.headMap(cand);
                    } else if (head.get(cand).firstKey() >= def) {
                        break;
                    } else {
                        int toRemove = head.get(cand).firstKey();

                        ret += head.get(cand).get(toRemove);
                        frontier.get(cand).remove(toRemove);
                    }
                }

                if (!frontier.containsKey(att))
                    frontier.put(att, new TreeMap<>());

                SortedMap<Integer, Integer> sameAtt = frontier.get(att);
                sameAtt.put(def, sameAtt.getOrDefault(def, 0) + 1);
            } else {
                ret += 1;
            }
        }

        return ret;
    }
}
