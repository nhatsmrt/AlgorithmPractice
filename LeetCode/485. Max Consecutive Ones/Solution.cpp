class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)

        int cnt = 0, ret = 0;

        for (int val : nums) {
            if (val == 1)
                cnt += 1;
            else {
                ret = max(ret, cnt);
                cnt = 0;
            }
        }

        return max(ret, cnt);
    }
};
