class Solution {
    public String crackSafe(int n, int k) {
        // Time Complexity: O(n k^n)
        StringBuilder ret = new StringBuilder();

        if (n == 1) {
            for (int i = 0; i < k; i++)
                ret.append((char) ('0' + i));
        }
        else {
            int numEdges = 1;
            for (int i = 0; i < n; i++)
                numEdges *= k;

            Queue<String> tour = new LinkedList<>();
            Map<String, Integer> next = new HashMap<>();

            String node = getInitial(n);

            while (tour.size() < numEdges) {
                int nextValue = next.getOrDefault(node, 0);
                while (nextValue == k) {
                    // stuck
                    String edge = tour.remove();
                    node = edge.substring(1);
                    tour.add(edge);
                    nextValue = next.getOrDefault(node, 0);
                }

                String edge = node + nextValue;
                next.put(node, nextValue + 1);
                tour.add(edge);
                node = edge.substring(1);
            }

            String edge = tour.remove();
            ret.append(edge);

            while (!tour.isEmpty()) {
                edge = tour.remove();
                ret.append(edge.charAt(edge.length() - 1));
            }
        }

        return ret.toString();
    }

    private String getInitial(int n) {
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < n - 1; i++)
            ret.append('0');

        return ret.toString();
    }
}
