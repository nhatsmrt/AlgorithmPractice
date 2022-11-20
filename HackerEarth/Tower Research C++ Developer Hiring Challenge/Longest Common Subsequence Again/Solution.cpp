#include<bits/stdc++.h>
using namespace std;

int solutions[500][500][11][11];


int memoized_lcs(string p, string s, int i, int j, int remain1, int remain2) {

      if (i == p.length() || j == s.length())
         return 0;

      if (solutions[i][j][remain1][remain2] != -1)
         return solutions[i][j][remain1][remain2];

      /* skip */
      int ret = max(
         memoized_lcs(p, s, i + 1, j, remain1, remain2),
         memoized_lcs(p, s, i, j + 1, remain1, remain2)
      );

      if (p[i] == s[j]) { /* match */
         ret = max(
            ret,
            1 + memoized_lcs(p, s, i + 1, j + 1, remain1, remain2)
         );
      } else {
         if (remain1 > 0) {
            ret = max(
               ret,
               1 + memoized_lcs(p, s, i + 1, j + 1, remain1 - 1, remain2)
            );
         }

         if (remain2 > 0) {
            ret = max(
               ret,
               1 + memoized_lcs(p, s, i + 1, j + 1, remain1, remain2 - 1)
            );
         }
      }

      solutions[i][j][remain1][remain2] = ret;
      return ret;
}

int LCS (string p, string s, int k1, int k2) {
   // Time and Space Complexity: O(MN * k1 * k2)
   // Write your code here
   for (int i = 0; i < p.length(); i++) {
      for (int j = 0; j < s.length(); j++) {
         for (int m = 0; m < k1 + 1; m++) {
            for (int n = 0; n < k2 + 1; n++)
               solutions[i][j][m][n] = -1;
         }
      }
   }

   return memoized_lcs(p, s, 0, 0, k1, k2);
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    getline(cin, s);
    string p;
    getline(cin, p);
    int k1;
    cin >> k1;
    int k2;
    cin >> k2;

    int out_;
    out_ = LCS(p, s, k1, k2);
    cout << out_;
}
