class Solution {
private:
    unordered_map<int, int> topo_sort(int k, vector<vector<int>>& conditions) {
        unordered_map<int, int> ret;
        unordered_map<int, vector<int>> adj_lists;
        unordered_map<int, int> incoming_cnter;

        for (int i = 1; i <= k; i++) {
            vector<int> neighs;
            adj_lists[i] = neighs;
            incoming_cnter[i] = 0;
        }

        for (vector<int> edge : conditions) {
            adj_lists[edge[0]].push_back(edge[1]);
            incoming_cnter[edge[1]] += 1;
        }

        vector<int> no_incoming;

        for (int i = 1; i <= k; i++) {
            if (incoming_cnter[i] == 0)
                no_incoming.push_back(i);
        }

        int order = 0;
        while (no_incoming.size() > 0) {
            int node = no_incoming.back();
            no_incoming.pop_back();

            ret[node] = order++;
            cout << ret[node];

            for (int neigh : adj_lists[node]) {
                incoming_cnter[neigh] -= 1;
                if (incoming_cnter[neigh] == 0)
                    no_incoming.push_back(neigh);
            }
        }

        return ret;
    }

public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        // Time Complexity: O(k^2)
        // Space Complexity: O(V + E) extra and O(k^2) for the result
        // where V = k, E = number of conditions

        vector<vector<int>> ret;
        unordered_map<int, int> row_order = topo_sort(k, rowConditions);
        unordered_map<int, int> col_order = topo_sort(k, colConditions);

        if (row_order.size() < k || col_order.size() < k)
            return ret;

        for (int i = 0; i < k; i++) {
            vector<int> row(k, 0);
            ret.push_back(row);
        }

        for (int i = 1; i <= k; i++) {
            ret[row_order[i]][col_order[i]] = i;
        }

        return ret;
    }
};
