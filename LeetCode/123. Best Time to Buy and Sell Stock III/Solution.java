class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1)
            return 0;

        List<Integer> pricesToConsider = new ArrayList<Integer>();
        boolean findPeak = false;
        int i = 0;
        while (i < prices.length) {
            if (findPeak) {
                if (prices[i] > prices[i - 1] && (i == prices.length - 1 || prices[i] >= prices[i + 1])) {
                    pricesToConsider.add(prices[i]);
                    findPeak = false;
                }
            }
            else {
                if ((i == 0 || prices[i] <= prices[i - 1]) && (i == prices.length - 1 || prices[i] < prices[i + 1])) {
                    pricesToConsider.add(prices[i]);
                    findPeak = true;
                }
            }
            i += 1;
        }

        if (pricesToConsider.size() <= 1)
            return 0;

        if (pricesToConsider.size() <= 3)
            return pricesToConsider.get(1) - pricesToConsider.get(0);

        if (pricesToConsider.size() <= 5)
            return pricesToConsider.get(1) - pricesToConsider.get(0) +
            pricesToConsider.get(3) - pricesToConsider.get(2);

        if (pricesToConsider.size() % 2 == 1) {
            pricesToConsider.remove(pricesToConsider.size() - 1);
        }

        int [] differences = new int[pricesToConsider.size() - 1];
        for (int j = 0; j < pricesToConsider.size() - 1; j++) {
            differences[j] = pricesToConsider.get(j + 1) - pricesToConsider.get(j);
        }

        int[] bestTo = new int[differences.length];
        int[] bestFrom = new int[differences.length];

        int curMax = 0;
        int maxToHere = 0;
        for (int j = 0; j < differences.length; j++) {
            maxToHere += differences[j];
            if (maxToHere < 0)
                maxToHere = 0;
            curMax = Math.max(curMax, maxToHere);
            bestTo[j] = curMax;
        }

        curMax = 0;
        int maxFromHere = 0;
        for (int j = differences.length - 1; j >= 0; j--) {
            maxFromHere += differences[j];
            if (maxFromHere < 0)
                maxFromHere = 0;
            curMax = Math.max(curMax, maxFromHere);
            bestFrom[j] = curMax;
        }

        curMax = 0;
        for (int j = 0; j < differences.length - 1; j++) {
            int candidate = bestTo[j] + bestFrom[j + 1];
            if (candidate > curMax)
                curMax = candidate;
        }

        return curMax;
    }
}
