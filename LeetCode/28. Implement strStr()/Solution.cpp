class Solution {
public:
    void compute_lps(string pattern, int ptrn_len, int *lps) {
        int longest_len = 0;
        lps[0] = 0;

        int ind = 1;
        while (ind < ptrn_len) {
            if (pattern[ind] == pattern[longest_len]) {
                longest_len += 1;
                lps[ind] = longest_len;
                ind += 1;
            }
            else {
                if (longest_len != 0)
                    longest_len = lps[longest_len - 1];
                else {
                    lps[ind] = 0;
                    ind += 1;
                }
            }
        }
    }

    int strStr(string haystack, string needle) {
        if (needle.length() == 0)
            return 0;

        int str_len = haystack.length();
        int ptrn_len = needle.length();

        int lps[ptrn_len];
        compute_lps(needle, ptrn_len, lps);

        int str_ind = 0;
        int pat_ind = 0;

        while (str_ind < str_len) {
            if (needle[pat_ind] == haystack[str_ind]) {
                pat_ind += 1;
                str_ind += 1;
            }

            if (pat_ind == ptrn_len)
                return str_ind - pat_ind;
            // Mismatch:
            else if (str_ind < str_len && needle[pat_ind] != haystack[str_ind]) {
                if (pat_ind != 0)
                    pat_ind = lps[pat_ind - 1];
                else
                    str_ind += 1;
            }
        }


        return -1;
    }
};
