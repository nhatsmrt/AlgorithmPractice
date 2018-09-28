/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {

    public int rand10() {
        boolean found = false;
        int candidate1, candidate2;
        int candidate = 0;


        while (!found) {
            candidate1 = rand7();
            candidate2 = rand7();

            candidate = ((candidate1 - 1) * 7 + candidate2) % 10 + 1;

            if (candidate1 <= 6 && (candidate1 != 6 || candidate2 <= 5))
                found = true;

        }

        return candidate;
    }

}
