class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = maxCandies(candies);
        vector<bool> ret;
        vector<int>::iterator it = candies.begin();

        while (it != candies.end()) {
            ret.push_back(*it + extraCandies >= max);
            it++;
        }

        return ret;
    }

private:
    int maxCandies(vector<int>& candies) {
        vector<int>::iterator it = candies.begin();
        int ret = 0;

        while (it != candies.end()) {
            ret = max(ret, *it);
            it++;
        }

        return ret;
    }
};
