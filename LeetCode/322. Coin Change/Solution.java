class Solution {
    HashMap<Integer, Integer> numCoins = new HashMap<Integer, Integer>();
    int minCoin;
    int maxCoin;

    public int coinChangeDP(int[] coins, int amount) {

        if (numCoins.containsKey(amount))
            return numCoins.get(amount);
        for (int coin : coins) {
            if (amount == coin) {
                numCoins.put(amount, 1);
                return 1;
            }
        }
        if (amount % maxCoin == 0) {
            numCoins.put(amount, amount / maxCoin);
            return amount / maxCoin;
        }

        ArrayList<Integer> candidates = new ArrayList<Integer>();
        for (int coin : coins) {
            if (amount - coin >= 0) {
                int numMoreCoin = coinChangeDP(coins, amount - coin);
                if (numMoreCoin >= 0)
                    candidates.add(numMoreCoin + 1);
                else
                    candidates.add(-1);
            }
        }

        int numCoin = -100;
        for (Integer candidate : candidates) {
            if ((numCoin < 0 && candidate > numCoin) || (numCoin >= 0 && candidate > 0 && candidate < numCoin))
                numCoin = candidate;
        }



        if (numCoin < 0)
            numCoin = -1;
        numCoins.put(amount, numCoin);
        return numCoin;
    }

    public int coinChange(int[] coins, int amount) {
        ArrayList<Integer> coinList = new ArrayList<Integer>();
        for (int coin : coins)
            coinList.add(coin);

        minCoin = Collections.min(coinList);
        maxCoin = Collections.max(coinList);
        if (minCoin > amount && amount > 0)
            return -1;

        if (amount % maxCoin == 0)
            return amount / maxCoin;

        numCoins.put(0, 0);
        for (int i = 1; i < minCoin; i++)
            numCoins.put(i, -1);
        numCoins.put(minCoin, 1);

        return coinChangeDP(coins, amount);
    }
}
