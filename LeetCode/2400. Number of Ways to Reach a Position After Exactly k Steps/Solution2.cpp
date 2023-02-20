class Solution {
private:
    const int MOD = 1000000007;
    const int INV_POW = MOD - 2;
    unordered_map<int, int> factorial_memo;

    // x^(-1) mod MOD == x^(MOD - 2) mod MOD
    long inverse(int value) {
        long ret = 1;
        long power = value;
        long exponent = INV_POW;

        while (exponent > 0) {
            if ((exponent & 1) > 0)
                ret = ret * power % MOD;

            exponent >>= 1;
            power = power * power % MOD;
        }

        return ret;
    }


    long factorial(int n) {
        if (n <= 1)
            return 1;

        if (factorial_memo.find(n) == factorial_memo.end())
            factorial_memo[n] = factorial(n - 1) * n % MOD;

        return factorial_memo[n];
    }
public:
    int numberOfWays(int startPos, int endPos, int k) {
        // Time Complexity O(K + log(MOD))
        // Space Complexity: O(K)

        int dist = abs(endPos - startPos);

        if (dist > k || (dist + k) % 2 == 1)
            return 0;

        int num_right = (k + dist) / 2;
        int num_left = (k - dist) / 2;
        // cout << num_right << " " << num_left << "\n";

        return factorial(k) * inverse(factorial(num_right) * factorial(num_left) % MOD) % MOD;
     }
};
