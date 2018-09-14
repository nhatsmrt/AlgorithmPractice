class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        HashMap<String, Integer> nodeIndMap = new HashMap<String, Integer>();
        ArrayList<HashMap<Integer, Double>> adjList = new ArrayList<HashMap<Integer, Double>> ();
        int numEquations = equations.length;

        int nodeInd = 0;
        for (int i = 0; i < numEquations; i++) {
            String[] equation = equations[i];

            if(!nodeIndMap.containsKey(equation[0])) {
                nodeIndMap.put(equation[0], nodeInd);
                nodeInd += 1;
                adjList.add(new HashMap<Integer, Double>());
            }
            if(!nodeIndMap.containsKey(equation[1])) {
                nodeIndMap.put(equation[1], nodeInd);
                nodeInd += 1;
                adjList.add(new HashMap<Integer, Double>());
            }

            int nodeInd0 = nodeIndMap.get(equation[0]);
            int nodeInd1 = nodeIndMap.get(equation[1]);

            adjList.get(nodeInd0).put(nodeInd1, values[i]);
            adjList.get(nodeInd1).put(nodeInd0, 1.0 / values[i]);

        }

        int numNodes = nodeIndMap.keySet().size();
        int numQueries = queries.length;
        double[] ret = new double[numQueries];

        for (int i = 0; i < numQueries; i++) {
            String[] query = queries[i];
            if (!nodeIndMap.containsKey(query[0]) || !nodeIndMap.containsKey(query[1])) {
                ret[i] = -1.0;
                continue;
            }

            int node1 = nodeIndMap.get(query[0]);
            int node2 = nodeIndMap.get(query[1]);

            if (node1 == node2)
                ret[i] = 1.0;
            else if (adjList.get(node1).containsKey(node2)) {
                ret[i] = adjList.get(node1).get(node2);
            }
            else {
                ArrayList<Integer> nodeList = new ArrayList(nodeIndMap.values());
                boolean found = false;
                while (!nodeList.isEmpty() && !found) {
                    Integer node = new Integer(node1);
                    for (int j = 0; j < nodeList.size(); j++) {
                        if (adjList.get(node1).containsKey(nodeList.get(j))) {
                            node = nodeList.get(j);
                            break;
                        }
                        else if (j == nodeList.size() - 1) {
                            ret[i] = -1.0;
                            found = true;
                        }
                    }

                    if (found)
                        break;

                    for (Integer neighbor : adjList.get(node).keySet()) {
                        if (nodeList.contains(neighbor)) {
                            adjList.get(node1).put(neighbor, adjList.get(node1).get(node) * adjList.get(node).get(neighbor));
                            if (neighbor == node2) {
                                ret[i] = adjList.get(node1).get(node) * adjList.get(node).get(neighbor);
                                found = true;
                                break;
                            }

                        }
                    }
                    nodeList.remove(node);
                }
            }
        }

        return ret;

    }
}
