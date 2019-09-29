class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        for (int stone : stones) {
            queue.add(-stone);
        }

        while (queue.size() > 1) {
            int stone1 = -queue.poll();
            int stone2 = -queue.poll();

            if (stone1 != stone2) {
                int newStone = stone1 > stone2 ? stone1 - stone2 : stone2 - stone1;
                queue.add(-newStone);
            }
        }

        if (queue.size() == 0)
            return 0;

        return -queue.poll();
    }
}
