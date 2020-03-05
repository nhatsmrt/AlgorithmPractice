class Solution {
    public int compress(char[] chars) {
        int insertPoint = 0;
        int it = 0;
        char cur = chars[0];
        int cnt = 0;

        while (it < chars.length) {
            if (chars[it] == cur) {
                it++;
                cnt++;
            }
            else {
                if (cnt == 1) {
                    chars[insertPoint] = cur;
                    insertPoint++;
                }
                else {
                    chars[insertPoint] = cur;
                    insertPoint++;
                    String cntStr = "" + cnt;
                    for (int i = 0; i < cntStr.length(); i++)
                        chars[insertPoint + i] = cntStr.charAt(i);

                    insertPoint += cntStr.length();
                }

                cur = chars[it];
                cnt = 0;
            }
        }

        if (cnt > 0) {
            if (cnt == 1) {
                chars[insertPoint] = cur;
                insertPoint++;
            }
            else {
                    chars[insertPoint] = cur;
                    insertPoint++;
                    String cntStr = "" + cnt;
                    for (int i = 0; i < cntStr.length(); i++)
                        chars[insertPoint + i] = cntStr.charAt(i);

                    insertPoint += cntStr.length();
            }
        }

        return insertPoint;
    }
}
