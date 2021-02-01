from functools import partial


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # Time and Space Complexity: O(N)

        def dist(point1: List[int], point2: List[int]):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        ret = 10000000000
        squir_to_nut_dists = list(map(partial(dist, squirrel), nuts))
        tree_to_nut_dists = list(map(partial(dist, tree), nuts))
        total_tree_to_nut = sum(tree_to_nut_dists)


        for i in range(len(nuts)):
            ret = min(
                ret,
                squir_to_nut_dists[i] + total_tree_to_nut * 2 - tree_to_nut_dists[i]
            )

        return ret
