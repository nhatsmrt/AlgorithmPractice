class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Time and Space Complexity: O(N)
        adjacent_lists = {}

        for pair in adjacentPairs:
            if pair[0] not in adjacent_lists:
                adjacent_lists[pair[0]] = []
            if pair[1] not in adjacent_lists:
                adjacent_lists[pair[1]] = []

            adjacent_lists[pair[0]].append(pair[1])
            adjacent_lists[pair[1]].append(pair[0])

        cur = None

        for num in adjacent_lists:
            if len(adjacent_lists[num]) == 1:
                cur = num
                break

        ret = [cur]
        used = set()
        used.add(cur)

        while len(ret) < len(adjacentPairs) + 1:
            if len(adjacent_lists[cur]) == 1:
                cur = adjacent_lists[cur][0]
            else:
                if adjacent_lists[cur][0] in used:
                    cur = adjacent_lists[cur][1]
                else:
                    cur = adjacent_lists[cur][0]

            used.add(cur)
            ret.append(cur)

        return ret
