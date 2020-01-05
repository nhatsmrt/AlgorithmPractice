import java.util.*;
import java.lang.*;
import java.io.*;
import java.text.DecimalFormat;

/* Name of the class has to be "Main" only if the class is public. */
class Solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] range = new int[n];
		for (int i = 0; i < n; i++)
			range[i] = sc.nextInt();

		double ret = 0.0;
		for (int a = 0; a < n; a++) {
			for (int b = a + 1; b < n; b++) {
				if (range[a] > range[b])
					ret += 1 - ((double) (range[b] + 1)) / (2 * range[a]);
				else
					ret += ((double) (range[a] - 1)) / (2 * range[b]);
			}
		}

		DecimalFormat df = new DecimalFormat("0.000000");
		System.out.println(df.format(ret));
	}
}
