class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ret;

        for (int i = 0; i < 2; i++) {
            for (auto it = nums.begin(); it != nums.end(); it++) {
                ret.push_back(*it);
            }
        }

        return ret;
    }
};
