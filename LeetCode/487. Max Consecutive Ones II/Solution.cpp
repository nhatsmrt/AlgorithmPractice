class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)

        int start = 0, end = 0;
        bool flipped = nums[0] == 0;
        int ret = 0;

        while (start < nums.size()) {
            if (end + 1 < nums.size() && (nums[end + 1] == 1 || !flipped)) {
                end += 1;
                flipped = flipped || nums[end] == 0;
            } else {
                ret = std::max(ret, end - start + 1);

                end += 1;
                if (end < nums.size()) {
                    // nums[end] == 0

                    while (start + 1 <= end && nums[start] == 1)
                        start += 1;
                    // found zero!
                    start += 1;
                    flipped = true;
                } else {
                    break;
                }
            }
        }

        return ret;
    }
};
