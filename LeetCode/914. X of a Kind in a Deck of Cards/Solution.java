class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        // Time Complexity: O(N log^2(N))
        // Space Complexity: O(N)

        Map<Integer, Integer> cnter = new HashMap<>();

        for (int value : deck) {
            cnter.put(value, cnter.getOrDefault(value, 0) + 1);
        }

        int gcdAll = cnter.get(deck[0]);

        for (int cnt : cnter.values()) {
            gcdAll = gcd(gcdAll, cnt);

            if (cnt == 1)
                return false;
        }

        return gcdAll > 1;
    }

    private int gcd(int fst, int snd) {
        if (fst == 1 || snd == 1)
            return 1;

        if (fst < snd)
            return gcd(snd, fst);

        if (snd % fst == 0)
            return fst;

        return gcd(snd, fst % snd);
    }
}
