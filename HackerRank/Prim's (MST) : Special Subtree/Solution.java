import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the prims function below.
    static int prims(int n, int[][] edges, int start) {
        if (n <= 1)
            return 0;

        int[][] adjMat = new int[n][n];
        for (int[] adjRow : adjMat)
            Arrays.fill(adjRow, 100000);

        for (int[] edge : edges) {
            adjMat[edge[0] - 1][edge[1] - 1] = adjMat[edge[1] - 1][edge[0] - 1]  = edge[2];
        }

        if (n == 2)
            return adjMat[0][1];

        int[] cost = new int[n];
        int[] edgeFrom = new int[n];
        Arrays.fill(cost, 100000);
        Arrays.fill(edgeFrom, -1);

        int ret = 0;
        ArrayList<Integer> verticesList = new ArrayList<Integer>();
        for (int i = 0; i < n; i++)
            verticesList.add(i);

        while(!verticesList.isEmpty()) {
            // find the node with minimum cost:
            int curMin = cost[verticesList.get(0)];
            Integer v = verticesList.get(0);
            for (int i = 0; i < verticesList.size(); i++) {
                Integer newVertex = verticesList.get(i);
                if (cost[newVertex] < curMin) {
                    curMin = cost[newVertex];
                    v = newVertex;
                }
            }


            verticesList.remove(v);
            if (edgeFrom[v] != -1)
                ret += cost[v];

            for (int i = 0; i < n; i++) {
                if (adjMat[v][i] != 100000 && verticesList.contains(i)) {
                    if (cost[i] > adjMat[v][i]) {
                        cost[i] = adjMat[v][i];
                        edgeFrom[i] = v;
                    }
                }
            }
        }


        return ret;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] edges = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] edgesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int edgesItem = Integer.parseInt(edgesRowItems[j]);
                edges[i][j] = edgesItem;
            }
        }

        int start = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int result = prims(n, edges, start);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
