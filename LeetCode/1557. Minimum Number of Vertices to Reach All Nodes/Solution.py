class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Time Complexity: O(V + E)
        # Space Complexity: O(V)

        candidates = set(range(n))

        for edge in edges:
            if edge[1] in candidates:
                candidates.remove(edge[1])

        return list(candidates)
