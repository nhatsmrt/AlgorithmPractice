class Solution {
private:
    int num_digit(int num) {
        int ret = 0;

        while (num > 0) {
            ret += 1;
            num /= 10;
        }

        return ret;
    }
public:
    int findNumbers(vector<int>& nums) {
        int ret = 0;

        for (int num : nums)
            ret += 1 - (num_digit(num) % 2);
        return ret;
    }
};
