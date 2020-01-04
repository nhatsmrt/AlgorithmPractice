/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.text.DecimalFormat;

/* Name of the class has to be "Main" only if the class is public. */
class Solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a = sc.nextInt();
		int b = sc.nextInt();

		double[][] dp = new double[n][6 * n + 1];
		for (int i = 0; i < dp.length; i++) {
			for (int j = 0; j < dp[0].length; j++)
				dp[i][j] = -1.0;
		}

		double ret = 0.0;
		for (int i = a; i <= b; i++)
			ret += probability(dp, n - 1, i);

		DecimalFormat df = new DecimalFormat("0.000000");
		System.out.println(df.format(ret));
	}

	private static double probability(double[][] dp, int n, int x) {
		if (x > 6 * (n + 1) || x == 0)
			return 0;

		if (n == 0)
			return ((float) 1) / 6;

		if (dp[n][x] >= 0.0)
			return dp[n][x];

		int lower = Math.max(1, x - 6);
		int upper = Math.min(x - 1, 6 * n);

		double ret = 0;
		for (int i = lower; i <= upper; i++)
			ret += probability(dp, n - 1, i);

		ret /= 6;
		dp[n][x] = ret;

		return ret;
	}
}
