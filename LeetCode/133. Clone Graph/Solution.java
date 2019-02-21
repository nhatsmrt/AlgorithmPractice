/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null)
            return node;

        return cloneGraph(node, new HashMap<Integer, UndirectedGraphNode>());
    }

    private UndirectedGraphNode cloneGraph(
        UndirectedGraphNode node,
        Map<Integer, UndirectedGraphNode> cloned
    ) {
        UndirectedGraphNode ret = new UndirectedGraphNode(node.label);
        cloned.put(node.label, ret);

        for (UndirectedGraphNode neighbor : node.neighbors) {
            if (neighbor.label == node.label)
                ret.neighbors.add(ret);
            else {
                UndirectedGraphNode neighborClone;

                if (cloned.containsKey(neighbor.label))
                    neighborClone = cloned.get(neighbor.label);
                else
                    neighborClone = cloneGraph(neighbor, cloned);

                ret.neighbors.add(neighborClone);
            }
        }

        return ret;
    }
}
