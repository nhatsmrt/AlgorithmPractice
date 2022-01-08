class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        // Time and Space Complexity: O(N)

        unordered_map<string, int> cnter1 = buildCnter(words1);
        unordered_map<string, int> cnter2 = buildCnter(words2);


        int ret = 0;
        for (auto pair : cnter1) {
            if (pair.second == 1 && cnter2.find(pair.first) != cnter2.end() && cnter2[pair.first] == 1)
                ret += 1;
        }

        return ret;
    }

private:
    unordered_map<string, int> buildCnter(vector<string>& words) {
        unordered_map<string, int> cnter;

        for (string word : words) {
            if (cnter.find(word) == cnter.end()) {
                cnter[word] = 1;
            } else {
                cnter[word] = cnter[word] + 1;
            }
        }

        return cnter;
    }
};
