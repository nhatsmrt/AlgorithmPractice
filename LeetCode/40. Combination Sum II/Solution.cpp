class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // Time Complexity: O(N^2 2^N)
        // Space Complexity: O(2^N)

        sort(candidates.begin(), candidates.end());

        vector<vector<int>> ret;
        vector<int> partial;

        backtrack(ret, candidates, 0, partial, target);
        return ret;
    }


private:
    void backtrack(
        vector<vector<int>>& ret, vector<int>& candidates, int pos,
        vector<int>& partial, int target
    ) {
        if (target == 0) {
            if (partial.size() > 0) {
                vector<int> solution;

                for (int i = 0; i < partial.size(); i++)
                    solution.push_back(partial[i]);

                ret.push_back(solution);
            }
        }
        else if (pos < candidates.size()) {
            // Not taking current number
            int newPos = pos;
            while (newPos < candidates.size() && candidates[newPos] == candidates[pos])
                newPos += 1;
            backtrack(ret, candidates, newPos, partial, target);

            if (candidates[pos] <= target) {
                partial.push_back(candidates[pos]);
                backtrack(ret, candidates, pos + 1, partial, target - candidates[pos]);
                partial.pop_back();
            }
        }
    }
};
