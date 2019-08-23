/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    private static int[][] dp;

	public static void main (String[] args) {
		//code
		Scanner sc = new Scanner(System.in);
		int numTest = sc.nextInt();
		for (int t = 0; t < numTest; t++) {
		    int nItem = sc.nextInt();
		    int maxWeight = sc.nextInt();

		    int[] values = new int[nItem];
		    int[] weights = new int[nItem];
		    for (int i = 0; i < nItem; i++)
		        values[i] = sc.nextInt();
		    for (int i = 0; i < nItem; i++)
		        weights[i] = sc.nextInt();

		    dp = new int[nItem][maxWeight + 1];
		    for (int i = 0; i < nItem; i++)
		        Arrays.fill(dp[i], -1);
		    System.out.println(subproblem(values, weights, 0, maxWeight));
		}
	}

	private static int subproblem(int[] values, int[] weights, int index, int remaining) {
	    if (index >= values.length)
	        return 0;
	   if (remaining == 0)
	        return 0;

	    if (dp[index][remaining] != -1)
	        return dp[index][remaining];


	    int ret = -1;
	    if (weights[index] > remaining)
	        ret = subproblem(values, weights, index + 1, remaining);
	    else {
	        int cand1 = subproblem(values, weights, index + 1, remaining);
	        int cand2 = values[index] +
	        subproblem(values, weights, index + 1, remaining - weights[index]);
	        ret = cand1 > cand2 ? cand1 : cand2;
	    }

	    dp[index][remaining] = ret;
	    return ret;
	}
}
