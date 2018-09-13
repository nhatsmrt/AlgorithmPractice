// based on https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        if (n == 0)
            return 0;
        else
            return 1 + hammingWeight(n & (n - 1));

    }
}
