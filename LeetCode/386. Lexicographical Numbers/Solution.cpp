class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> ret;
        for (int i = 1; i < 10; i++) {
            build(i, n, ret);
        }

        return ret;
    }

private:
    void build(int cur, int bound, vector<int> &ret) {
        if (cur <= bound) {
            ret.push_back(cur);
            cur *= 10;
            for (int i = 0; i < 10; i++)
                build(cur + i, bound, ret);
        }
    }
};
