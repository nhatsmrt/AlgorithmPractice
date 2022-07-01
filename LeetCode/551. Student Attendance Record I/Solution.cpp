class Solution {
public:
    bool checkRecord(string s) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)

        int consec_late = 0;
        int abs_cnt = 0;

        for (auto c : s) {
            if (c == 'L')
                consec_late += 1;
            else
                consec_late = 0;

            if (c == 'A')
                abs_cnt += 1;

            if (consec_late == 3)
                return false;
        }


        return abs_cnt < 2;
    }
};
