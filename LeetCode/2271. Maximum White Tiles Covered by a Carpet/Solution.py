class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Time and Space Complexity: O(N log N)

        # Analysis: each tile is added once onto the deque
        # and remove (in entirety) at most once
        # Re-addition is possible, but it only happens once
        # per iteration of the outer loop.

        tiles.sort()
        in_range = deque()

        ret = 0
        area_covered = 0

        for start, end in tiles:
            while in_range and in_range[0][0] + carpetLen <= end:
                # each tile is added and removed (in entirety) at most once!
                old_start, old_end = in_range.popleft()
                area_covered -= old_end - old_start + 1

                if old_end + carpetLen > end: # not remove entire piece
                    # This steps happens at most once per (start, end)!
                    in_range.appendleft((end - carpetLen + 1, old_end))
                    area_covered += in_range[0][1] - in_range[0][0] + 1

            start = max(start, end - carpetLen + 1)
            in_range.append((start, end))
            area_covered += end - start + 1
            ret = max(ret, area_covered)

        return ret
