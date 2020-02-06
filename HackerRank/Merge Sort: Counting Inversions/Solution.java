import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the countInversions function below.
    private static Long ret;
    static long countInversions(int[] arr) {
        ret = new Long(0);
        countInversions(arr, 0, arr.length - 1);
        return ret;
    }

    static int[] countInversions(int[] arr, int start, int end) {
        if (start == end)
            return new int[] {arr[start]};

        int mid = (start + end) / 2;
        int[] left = countInversions(arr, start, mid);
        int[] right = countInversions(arr, mid + 1, end);
        int[] retArr = new int[end - start + 1];

        int it1 = 0;
        int it2 = 0;
        int ind = 0;

        while (it1 <= left.length - 1 && it2 <= right.length - 1) {
            if (left[it1] <= right[it2]) {
                retArr[ind] = left[it1];
                it1 += 1;
                ind += 1;
            }
            else {
                ret += (left.length - it1);
                retArr[ind] = right[it2];
                it2 += 1;
                ind += 1;
            }
        }

        for (int i = it1; i < left.length; i++) {
            retArr[ind] = left[i];
            ind += 1;
        }

        for (int i = it2; i < right.length; i++) {
            retArr[ind] = right[i];
            ind += 1;
        }

        return retArr;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] arr = new int[n];

            String[] arrItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int arrItem = Integer.parseInt(arrItems[i]);
                arr[i] = arrItem;
            }

            long result = countInversions(arr);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
