import java.util.AbstractMap;

class Solution {
    public int minimumOperations(int[] nums, int start, int goal) {
        // Time and Space Complexity: O(V + E)

        Set<Integer> visited = new HashSet<>();
        Queue<Map.Entry<Integer, Integer>> traverse = new ArrayDeque<>();

        traverse.add(new AbstractMap.SimpleEntry<>(start, 0));
        visited.add(start);

        while (!traverse.isEmpty()) {
            Map.Entry<Integer, Integer> valueAndLevel = traverse.remove();
            int value = valueAndLevel.getKey();
            int level = valueAndLevel.getValue();

            if (value == goal)
                return level;

            for (int num : nums) {
                int neighbors[] = {
                    value + num,
                    value - num,
                    value ^ num,
                };

                for (int neigh : neighbors) {
                    if (!visited.contains(neigh) && (neigh == goal || (0 <= neigh && neigh <= 1000))) {
                        visited.add(neigh);
                        traverse.add(new AbstractMap.SimpleEntry<>(neigh, level + 1));
                    }
                }
            }
        }

        return -1;
    }
}
