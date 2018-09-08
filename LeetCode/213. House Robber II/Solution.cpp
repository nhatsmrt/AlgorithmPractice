class Solution {
    map<string, int> lookup;
public:
    int helper(vector<int>&nums, int start) {
        int nums_size = nums.size();
        if (nums_size == 0)
            return 0;
        string key = "";
        int sol = 0;
        for (int i = 0; i < nums_size; i++) {
            key += to_string(nums[i]);
        }
        key += to_string(start);

        if(lookup.find(key) != lookup.end())
            return lookup[key];

        if (start == 1) {
            if (nums_size == 1) {
            lookup[key] = nums[0];
            return nums[0];
            }

            if(nums_size == 2) {
                lookup[key] = max(nums[0], nums[1]);
                return lookup[key];
            }

            if (nums_size == 3){
                lookup[key] = max(nums[0], max(nums[1], nums[2]));
                return lookup[key];
            }

            else {
                vector<int> subvector1(nums.begin() + 1, nums.begin() + nums_size - 2);
                vector<int> subvector2(nums.begin(), nums.begin() + nums_size - 1);
                sol = max(helper(subvector1, 0) + nums[nums_size - 1], helper(subvector2, 0));
                lookup[key] = sol;
            }
            lookup[key] = sol;
            return sol;

        }
        else {
            if (nums_size == 1) {
                lookup[key] = nums[0];
                return nums[0];
            }

            if(nums_size == 2) {
                lookup[key] = max(nums[0], nums[1]);
                return lookup[key];
            }

            else {
                vector<int> subvector1(nums.begin(), nums.begin() + nums_size - 2);
                vector<int> subvector2(nums.begin(), nums.begin() + nums_size - 1);
                sol = max(helper(subvector1, 0) + nums[nums_size - 1], helper(subvector2, 0));
                lookup[key] = sol;
            }
            lookup[key] = sol;
            return sol;
        }
        return 0;

    }
    int rob(vector<int>& nums) {
        return helper(nums, 1);
    }
};
