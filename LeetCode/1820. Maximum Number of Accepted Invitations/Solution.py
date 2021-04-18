class Solution:
    def match(self, boy: int, grid: List[List[int]], matched: dict, seen: set) -> bool:
        for girl in range(len(grid[0])):
            if grid[boy][girl] and girl not in seen:
                seen.add(girl)

                if girl not in matched or self.match(matched[girl], grid, matched, seen):
                    matched[girl] = boy
                    return True

        return False

    def maximumInvitations(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(V(V + E))
        # Space Complexity: O(V + E)

        matched = {}

        for boy in range(len(grid)):
            self.match(boy, grid, matched, set())

        return len(matched)
