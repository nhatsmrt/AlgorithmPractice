class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] in_degree = new int[numCourses];
        int[][] adjMat = new int[numCourses][numCourses];
        int[] ordering = new int[numCourses];
        boolean[] visited = new boolean[numCourses];
        Arrays.fill(in_degree, 0);
        for (int[] row : adjMat)
            Arrays.fill(row, 0);
        Arrays.fill(visited, false);

        for (int i = 0; i < prerequisites.length; i++) {
            in_degree[prerequisites[i][0]] += 1;
            adjMat[prerequisites[i][1]][prerequisites[i][0]] = 1;
        }

        Deque<Integer> traverseQueue = new ArrayDeque<Integer>();
        for (int i = 0; i < numCourses; i++) {
            if (in_degree[i] == 0) {
                traverseQueue.addLast(i);
                visited[i] = true;
            }
        }

        int numCoursesAdded = 0;
        while(!traverseQueue.isEmpty()) {
            int node = traverseQueue.removeFirst();
            for (int i = 0; i < numCourses; i++) {
                if (adjMat[node][i] == 1 && !visited[i]) {
                    in_degree[i] -= 1;
                    if (in_degree[i] == 0) {
                        traverseQueue.addLast(i);
                        visited[i] = true;
                    }
                }
            }
            ordering[numCoursesAdded] = node;
            numCoursesAdded += 1;
        }

        if (numCoursesAdded < numCourses)
            return new int[0];
        return ordering;
    }
}
