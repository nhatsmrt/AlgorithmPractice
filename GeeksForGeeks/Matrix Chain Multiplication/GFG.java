/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    private static int [][] dp;

	public static void main (String[] args) {
		//code
		Scanner sc = new Scanner(System.in);
		int nTest = sc.nextInt();
		for (int i = 0; i < nTest; i++) {
		    int nNum = sc.nextInt();
		    int[] matSizes = new int[nNum];
		    for (int j = 0; j < nNum; j++)
		        matSizes[j] = sc.nextInt();
		    dp = new int[nNum][nNum];
		    for (int k = 0; k < dp.length; k++) {
		        Arrays.fill(dp[k], -1);
		    }
		    System.out.println(cost(matSizes, 0, nNum - 1));
		}
	}

	private static int cost(int[] matSizes, int i, int j) {
	   // int ret = 0;
	   // if (i)
	   //return 0;
	   if (dp[i][j] != -1)
	       return dp[i][j];
	   else {
	       int ret = 0;
	       if (i + 2 == j) {
	           ret = matSizes[i] * matSizes[i + 1] * matSizes[i + 2];
	       }
	       else if (i < j - 2) {
	           ret = -1;
	           for (int k = i + 1; k <= j - 1; k++) {
	               int candidate = cost(matSizes, i, k)
	               + cost(matSizes, k, j)
	               + matSizes[i] * matSizes[k] * matSizes[j];
	               if (ret == -1 || candidate < ret)
	                   ret = candidate;
	           }
	       }
	       dp[i][j] = ret;
	       return ret;
	   }
	}
}
