class Solution {
    public int findMaximizedCapital(int k, int W, int[] Profits, int[] Capital) {
        // Greedy; while can still add projects, choose the most profitable
        // project that your capital allows
        // Time Complexity: O(N log N)

        int ret = W;
        PriorityQueue<Integer> capitalHeap = new PriorityQueue<>(new ByCapitalComparator(Capital));
        PriorityQueue<Integer> profitHeap = new PriorityQueue<>(new ByProfitComparator(Profits));
        int projectAdded = 0;


        for (int i = 0; i < Profits.length; i++)
            capitalHeap.add(i);

        while(
            projectAdded < k &&
            !capitalHeap.isEmpty() &&
            Capital[capitalHeap.peek()] <= ret
        ) {
            while(!capitalHeap.isEmpty() && Capital[capitalHeap.peek()] <= ret)
                profitHeap.offer(capitalHeap.poll());

            int project = profitHeap.poll();
            ret += Profits[project];
            projectAdded += 1;
        }

        if (projectAdded < k) {
            for (int i = 0; i < k - projectAdded; i++) {
                if (!profitHeap.isEmpty())
                    ret += Profits[profitHeap.poll()];
                else
                    break;
            }

        }
        // System.out.println(profitHeap);
        return ret;
    }

    private class ByCapitalComparator implements Comparator<Integer> {
        private int[] capitals;

        public ByCapitalComparator(int[] capitals) {this.capitals = capitals;}

        public int compare(Integer project1, Integer project2) {
            return Integer.compare(capitals[project1], capitals[project2]);
        }
    }

    private class ByProfitComparator implements Comparator<Integer> {
        private int[] profits;

        public ByProfitComparator(int[] profits) {this.profits = profits;}

        public int compare(Integer project1, Integer project2) {
            return -Integer.compare(profits[project1], profits[project2]);
        }
    }
}
