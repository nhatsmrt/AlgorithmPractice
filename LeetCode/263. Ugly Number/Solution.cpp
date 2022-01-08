class Solution {
public:
    bool isUgly(int n) {
        // Time Complexity: O(log n)
        // Space Complexity: O(1)

        if (n <= 0)
            return false;

        int divisors[3] = { 2, 3, 5 };

        for (int divisor : divisors) {
            while (n != 0 && n % divisor == 0)
                n /= divisor;
        }

        return n == 1;
    }
};
