class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sorted(nums);
        sort(sorted.begin(), sorted.end());
        vector<int> ret;

        vector<int>::iterator it = nums.begin();
        while (it != nums.end()) {
            ret.push_back(find(sorted.begin(), sorted.end(), *it) - sorted.begin());
            it++;
        }

        return ret;
    }
};
