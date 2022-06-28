class Solution {
public:
    bool checkIfPangram(string sentence) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)

        unordered_set<char> contains;

        for (auto it = sentence.begin(); it != sentence.end(); it++) {
            contains.insert({*it});
        }

        return contains.size() == 26;
    }
};
