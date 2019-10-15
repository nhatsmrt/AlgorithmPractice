import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {
    private static int[][][] dp;
    // Complete the abbreviation function below.
    static String abbreviation(String a, String b) {
        dp = new int[a.length()][b.length()][3];
        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++)
                dp[i][j][0] = dp[i][j][1] = dp[i][j][2] = -1;
        }
        if (
            abbreviation(a, b, 0, 0, 0) == 1 ||
            abbreviation(a, b, 0, 0, 1) == 1 ||
            abbreviation(a, b, 0, 0, 2) == 1
            )
            return "YES";

        return "NO";
    }

    private static int abbreviation(String a, String b, int pos1, int pos2, int action) {
        if (pos1 == a.length()) {
            if (pos2 == b.length())
                return 1;

            return 0;
        }

        if (pos2 == b.length()) {
            if (action == 2 && a.charAt(pos1) >= 'a' && a.charAt(pos1) <= 'z')
                return abbreviation(a, b, pos1 + 1, pos2, 2);

            return 0;
        }

        if (dp[pos1][pos2][action] != -1)
            return dp[pos1][pos2][action];

        int ret = 0;
        if (action == 0) { // keep
            if (
                a.charAt(pos1) == b.charAt(pos2) &&
                a.charAt(pos1) >= 'A' && a.charAt(pos1) <= 'Z' &&
                (
                    abbreviation(a, b, pos1 + 1, pos2 + 1, 0) == 1 ||
                    abbreviation(a, b, pos1 + 1, pos2 + 1, 1) == 1 ||
                    abbreviation(a, b, pos1 + 1, pos2 + 1, 2) == 1
                )
            )
                ret = 1;
        }
        else if (a.charAt(pos1) >= 'a' && a.charAt(pos1) <= 'z') {
            if (action == 1) { // capitalize
                if (
                    (char) (a.charAt(pos1) + ('A' - 'a')) == b.charAt(pos2) &&
                    (
                        abbreviation(a, b, pos1 + 1, pos2 + 1, 0) == 1 ||
                        abbreviation(a, b, pos1 + 1, pos2 + 1, 1) == 1 ||
                        abbreviation(a, b, pos1 + 1, pos2 + 1, 2) == 1
                    )
                )
                    ret = 1;
            }
            else { // delete character
                if (
                    abbreviation(a, b, pos1 + 1, pos2, 0) == 1 ||
                    abbreviation(a, b, pos1 + 1, pos2, 1) == 1 ||
                    abbreviation(a, b, pos1 + 1, pos2, 2) == 1
                )
                    ret = 1;
            }
        }

        dp[pos1][pos2][action] = ret;
        return ret;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String a = scanner.nextLine();

            String b = scanner.nextLine();

            String result = abbreviation(a, b);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
