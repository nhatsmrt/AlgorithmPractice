from sortedcontainers import SortedSet


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        nearest_larger = []
        nearest_smaller = []

        sorted_set = SortedSet()
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]

            if sorted_set:
                ind = sorted_set.bisect_left((val, -i))

                if ind == 0:
                    nearest_smaller.append(len(arr))
                else:
                    nearest_smaller.append(-sorted_set[ind - 1][1])
            else:
                nearest_smaller.append(len(arr))

            sorted_set.add((val, -i))

        nearest_smaller = nearest_smaller[::-1]

        sorted_set = SortedSet()
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]

            if sorted_set:
                ind = sorted_set.bisect_left((-val, -i))

                if ind == 0:
                    nearest_larger.append(len(arr))
                else:
                    nearest_larger.append(-sorted_set[ind - 1][1])
            else:
                nearest_larger.append(len(arr))

            sorted_set.add((-val, -i))

        nearest_larger = nearest_larger[::-1]

        dp = {}

        def reachable(index: int, is_even: bool):
            if (index, is_even) in dp:
                return dp[(index, is_even)]

            if index == len(arr) - 1:
                return True

            next_arr = nearest_smaller if is_even else nearest_larger
            ret = next_arr[index] < len(arr) and reachable(next_arr[index], not is_even)

            dp[(index, is_even)] = ret
            return ret

        ret = 0
        for i in range(len(arr)):
            ret += int(reachable(i, False))

        return ret
