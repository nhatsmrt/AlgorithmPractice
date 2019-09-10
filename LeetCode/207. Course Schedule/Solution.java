class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {


        Map<Integer, List<Integer>> adjacencyList = new HashMap<Integer, List<Integer>>();
        for (int[] edge : prerequisites) {
            if (!adjacencyList.containsKey(edge[0]))
                adjacencyList.put(edge[0], new ArrayList<Integer>());
            adjacencyList.get(edge[0]).add(edge[1]);
        }

        Set<Integer> unvisited = new HashSet<Integer>();
        for (int i = 0; i < numCourses; i++)
            unvisited.add(i);
        Stack<Integer> traverseStack = new Stack<Integer>();
        Set<Integer> descendancy = new HashSet<Integer>();

        while (!unvisited.isEmpty() || !traverseStack.isEmpty()) {
            if (traverseStack.isEmpty()) {
                int node = remove(unvisited);
                traverseStack.add(node);
                // descendancy = new HashSet<Integer>();
            }
            else {
                int node = traverseStack.peek();
                if (!descendancy.contains(node)) {
                    descendancy.add(node);
                    if (adjacencyList.containsKey(node)) {
                        for (Integer next : adjacencyList.get(node)) {
                            if (descendancy.contains(next))
                                return false; // detect back edge
                            else if (unvisited.contains(next)) {
                                unvisited.remove(next);
                                traverseStack.add(next);
                            }
                        }
                    }
                }
                else {
                    traverseStack.pop();
                    descendancy.remove(node);
                }
            }
        }

        return true;
    }

    private int remove(Set<Integer> set) {
        Iterator<Integer> it = set.iterator();
        if (!it.hasNext())
            return -1;

        int next = it.next();
        it.remove();
        return next;
    }
}
