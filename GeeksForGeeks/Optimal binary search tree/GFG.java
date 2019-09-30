/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    private static int[] freqsPrefix;
    private static int[][] dp;

	public static void main (String[] args) {
		//code
		Scanner sc = new Scanner(System.in);
		int numTest = sc.nextInt();
		for (int t = 0; t < numTest; t++) {
	    int numNodes = sc.nextInt();
	    int[] keys = new int[numNodes];
	    int[] freqs = new int[numNodes];

	    for(int i = 0; i < numNodes; i++)
            keys[i] = sc.nextInt();
      for (int i = 0; i < numNodes; i++)
          freqs[i] = sc.nextInt();

	    freqsPrefix = new int[numNodes + 1];
	    freqsPrefix[0] = 0;
	    dp = new int[numNodes][numNodes];
	    for (int i = 0; i < numNodes; i++)
	        Arrays.fill(dp[i], -1);

	    for (int i = 0; i < numNodes; i++)
	        freqsPrefix[i + 1] = freqsPrefix[i] + freqs[i];

	    System.out.println(minSub(keys, freqs, 0, numNodes - 1));
		}

	}

	private static int minSub(int[] keys, int[] freqs, int i, int j) {
	    if (dp[i][j] != -1)
	        return dp[i][j];
	    else if (i == j)
	        return freqs[i];

	    int ret = -1;
	    for (int r = i; r <= j; r++) {
	        int candidate = 0;
	        if (r > i)
	            candidate += minSub(keys, freqs, i, r - 1);
	        if (r < j)
	            candidate += minSub(keys, freqs, r + 1, j);
	        if (ret == -1 || candidate < ret)
	            ret = candidate;
	    }
	    dp[i][j] = ret + freqsPrefix[j + 1] - freqsPrefix[i];
	    return dp[i][j];
	}

}
