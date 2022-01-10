class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        // Time Complexity: O(log N)
        // Space Complexity: O(1)

        auto it = std::upper_bound(letters.begin(), letters.end(), target);
        return it == letters.end() ? letters[0] : *it;
    }
};
