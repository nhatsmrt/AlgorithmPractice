public class Solution extends Relation {

    public int findCelebrity(int n) {
        int candidate = 0;

        for (int i = 1; i < n; i++) {
            if (super.knows(candidate, i))
                candidate = i;
        }
        // n checks
        // for all i > candidate, candidate does not know o

        for (int i = 0; i < candidate; i++) {
            if (super.knows(candidate, i) || !super.knows(i, candidate))
                return -1;
        }
        // for all i < candidate, candidate does not know i and i knows candidate
        // candidate check

        for (int i = candidate + 1; i < n; i++) {
            if (!super.knows(i, candidate))
                return -1;
        }
        // for all i > candidate, i knows candidate
        // n - 1 - candidate checks

        // total number of checks: 2n - 1 = Theta(n)

        return candidate;
    }

}
