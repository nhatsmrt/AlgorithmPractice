class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        start = 0
        end = 0
        ret = 0

        while start < len(seats):
            if seats[start] == 1:
                start += 1
                end = start
            elif end + 1 < len(seats) and seats[end + 1] == 0:
                end += 1
            else:
                if not start:
                    candidate = end + 1
                elif end + 1 == len(seats):
                    candidate = end + 1 - start
                else:
                    candidate = (end - start + 2) // 2

                ret = max(ret, candidate)


                start = end + 1
                end = start

        return ret
