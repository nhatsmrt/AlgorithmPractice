class Solution {
public:
    vector<long long> minimumCosts(vector<int>& regular, vector<int>& express, int expressCost) {
        // Time Complexity: O(N)
        // Space Complexity: O(1) extra space, O(N) for answer
        vector<long long> ret;
        long long reg_cost = regular[0], expr_cost = expressCost + express[0];
        long long new_reg_cost, new_expr_cost;

        ret.push_back(min(reg_cost, expr_cost));

        for (int i = 1; i < regular.size(); i++) {
            new_reg_cost = min(reg_cost, expr_cost) + regular[i];
            new_expr_cost = min(reg_cost + expressCost, expr_cost) + express[i];

            reg_cost = new_reg_cost;
            expr_cost = new_expr_cost;

            ret.push_back(min(reg_cost, expr_cost));
        }

        return ret;
    }
};
