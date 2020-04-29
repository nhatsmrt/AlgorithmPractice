from collections import deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Time and Space Complexity: O(N)

        if len(arr) == 1:
            return 0

        index = {}

        for i in range(len(arr)):
            if arr[i] not in index:
                index[arr[i]] = set()

            index[arr[i]].add(i)

        visited = {0}
        cur_level = {0}
        index[arr[0]].remove(0)
        level = 0

        while len(cur_level) > 0:
            next_level = set()

            for ind in cur_level:
                if ind > 0 and ind - 1 not in visited:
                    next_level.add(ind - 1)
                    visited.add(ind - 1)
                if ind + 1 < len(arr) and ind + 1 not in visited:
                    next_level.add(ind + 1)
                    visited.add(ind + 1)

                for neighbor in index.get(arr[ind], []):
                    if neighbor not in visited:
                        next_level.add(neighbor)
                        visited.add(neighbor)


            if len(arr) - 1 in next_level:
                return level + 1

            for ind in next_level:
                index[arr[ind]].remove(ind)

            level += 1
            cur_level = next_level

        return -1
