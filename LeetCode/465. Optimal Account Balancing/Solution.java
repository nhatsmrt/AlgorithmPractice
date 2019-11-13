class Solution {
    public int minTransfers(int[][] transactions) {
        // observation 1: it does not matter who owes whom money,
        // only the total balance of each person, from which we can
        // transfer money around to cancel out
        Map<Integer, Integer> balance = new HashMap<Integer, Integer>();
        for (int[] transaction : transactions) {
            balance.put(
                transaction[0], balance.getOrDefault(transaction[0], 0) - transaction[2]
            );
            balance.put(
                transaction[1], balance.getOrDefault(transaction[1], 0) + transaction[2]
            );
        }
        // observation 2: only the people with non-zero balance should be considered:
        List<Integer> nonZeroBalance = new ArrayList<Integer>();
        for (int amount : balance.values()) {
            if (amount != 0)
                nonZeroBalance.add(amount);
        }
        return clearDebt(nonZeroBalance);
    }

    private int clearDebt(List<Integer> balance) {
        if (balance.size() == 0)
            return 0;

        int numRemain = balance.size() - 1;
        if (balance.get(numRemain) == 0) {
            balance.remove(numRemain);
            int ret = clearDebt(balance);
            balance.add(0);
            return ret;
        }

        int ret = -1;

        int end = balance.remove(numRemain);
        boolean found = false;

        // optimization: if we found one cancellable debt, cancel them right away
        for (int i = 0; i < balance.size(); i++) {
            if (balance.get(i) == -end) {
                balance.set(i, 0);
                ret = 1 + clearDebt(balance);
                balance.set(i, -end);
                found = true;
                break;
            }
        }

        if (!found) {
            for (int i = 0; i < balance.size(); i++) {
                if (end * balance.get(i) < 0) {
                    // try to clear debt
                    balance.set(i, end + balance.get(i));
                    // recursion
                    int candidate = 1 + clearDebt(balance);
                    if (ret == -1 || ret > candidate)
                        ret = candidate;
                    // untry backtrack:
                    balance.set(i, balance.get(i) - end);
                }
            }
        }
        balance.add(end);

        return ret;
    }
}
