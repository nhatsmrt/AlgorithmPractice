class Node {
    private int cnt;
    private int minRange;
    private int maxRange;
    private Node left;
    private Node right;

    public Node(int minRange, int maxRange) {
        this.minRange = minRange;
        this.maxRange = maxRange;
        cnt = 0;
        left = null;
        right = null;
    }

    public void insert(int value) {
        cnt += 1;

        if (minRange != maxRange) {
            int midPoint = minRange + (maxRange - minRange) / 2;

            if (value <= midPoint) {
                if (left == null)
                    left = new Node(minRange, midPoint);

                left.insert(value);
            }
            else {
                if (right == null)
                    right = new Node(midPoint + 1, maxRange);

                right.insert(value);
            }
        }
    }

    public int query(int value) {
        if (minRange >= value)
            return 0;

        if (maxRange < value)
            return cnt;

        int ret = 0;

        if (left != null)
            ret += left.query(value);

        if (right != null)
            ret += right.query(value);

        return ret;
    }
}


class Solution {
    public int createSortedArray(int[] instructions) {
        // Time Complexity: O(N log N)
        // Space Complexity: O(N)

        // coordinate compression:
        int[] sortedInstructions = Arrays.copyOf(instructions, instructions.length);

        Arrays.sort(sortedInstructions);
        Map<Integer, Integer> index = new HashMap<>();

        for (int instruction : sortedInstructions) {
            if (!index.containsKey(instruction))
                index.put(instruction, index.size());
        }

        int ret = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        Node root = new Node(0, index.size() - 1);
        int totalCnt = 0;
        int MOD = 1000000007;


        for (int instruction : instructions) {
            int ind = index.get(instruction);
            int lessThan = root.query(ind);
            int greaterThan = totalCnt - lessThan - counter.getOrDefault(ind, 0);

            ret += Math.min(lessThan, greaterThan);
            ret = ret % MOD;

            root.insert(ind);
            counter.put(ind, counter.getOrDefault(ind, 0) + 1);
            totalCnt += 1;
        }

        return ret;
    }
}
