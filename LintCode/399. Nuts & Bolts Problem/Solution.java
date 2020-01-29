/**
 * public class NBCompare {
 *     public int cmp(String a, String b);
 * }
 * You can use compare.cmp(a, b) to compare nuts "a" and bolts "b",
 * if "a" is bigger than "b", it will return 1, else if they are equal,
 * it will return 0, else if "a" is smaller than "b", it will return -1.
 * When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
*/
public class Solution {
    /**
     * @param nuts: an array of integers
     * @param bolts: an array of integers
     * @param compare: a instance of Comparator
     * @return: nothing
     */

    private Random randomizer;
    public void sortNutsAndBolts(String[] nuts, String[] bolts, NBComparator compare) {
        // write your code here
        // Expected Runtime: O(n log n)
        // Space Complexity: O(1) (in place)
        randomizer = new Random();
        sortNutsAndBolts(nuts, bolts, compare, 0, nuts.length - 1);
    }

    private void sortNutsAndBolts(String[] nuts, String[] bolts, NBComparator compare, int start,  int end) {
        if (start < end) {
            int nutInd = start + randomizer.nextInt(end - start + 1);
            int boltInd = -1;
            for (int i = start; i <= end; i++) {
                if (compare.cmp(nuts[nutInd], bolts[i]) == 0) {
                    boltInd = i;
                    break;
                }
            }

            swap(nuts, nutInd, end);
            swap(bolts, boltInd, end);

            int firstRight = start;
            // Lomuto Partitioning
            for (int i = start; i < end; i++) {
                if (compare.cmp(nuts[i], bolts[end]) < 0) {
                    swap(nuts, i, firstRight);
                    firstRight += 1;
                }
            }
            swap(nuts, firstRight, end);
            int pivot = firstRight;

            // Lomuto Partitioning
            firstRight = start;
            for (int i = start; i < end; i++) {
                if (compare.cmp(nuts[pivot], bolts[i]) > 0) {
                    swap(bolts, i, firstRight);
                    firstRight += 1;
                }
            }
            swap(bolts, pivot, end);

            sortNutsAndBolts(nuts, bolts, compare, start, pivot - 1);
            sortNutsAndBolts(nuts, bolts, compare, pivot + 1, end);
        }
    }

    private void swap(String[] arr, int i, int j) {
        String tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
};
