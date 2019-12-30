class Solution {
    public boolean canReach(int[] arr, int start) {
        Set<Integer> zeroSet = new HashSet<>();
        Map<Integer, Set<Integer>> adjLists = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0)
                zeroSet.add(i);
            else {
                int first = i - arr[i];
                int second = i + arr[i];
                if (first >= 0 || second < arr.length) {
                    adjLists.put(i, new HashSet<>());
                    Set<Integer> neighbors = adjLists.get(i);
                    if (first >= 0)
                        neighbors.add(first);
                    if (second < arr.length)
                        neighbors.add(second);
                }
            }
        }

        if (zeroSet.isEmpty())
            return false;

        Set<Integer> visited = new HashSet<>();
        return canReach(start, adjLists, visited, zeroSet);
    }

    private boolean canReach(int node, Map<Integer, Set<Integer>> adjLists, Set<Integer> visited, Set<Integer> zeroSet) {
        if (zeroSet.contains(node))
            return true;

        if (!adjLists.containsKey(node))
            return false;

        Set<Integer> neighbors = adjLists.get(node);
        for (Integer neighbor : neighbors) {
            if (!visited.contains(neighbor)) {
                visited.add(neighbor);
                if (canReach(neighbor, adjLists, visited, zeroSet))
                    return true;
            }
        }

        return false;
    }
}
