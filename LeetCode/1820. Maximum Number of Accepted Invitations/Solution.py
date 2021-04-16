class Solution:
    def match(self, boy: int, adj_lists: dict, matched_boy: set, matched_girl: dict, seen: set) -> bool:
        for girl in adj_lists[boy]:
            if girl not in seen:
                seen.add(girl)

                if girl not in matched_girl or self.match(matched_girl[girl], adj_lists, matched_boy, matched_girl, seen):
                    matched_girl[girl] = boy
                    matched_boy.add(boy)
                    return True

        return False

    def maximumInvitations(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(V(V + E))
        # Space Complexity: O(V + E)

        matched_girl = {}
        matched_boy = set()
        adj_lists = {boy: set([girl for girl in range(len(grid[0])) if grid[boy][girl]]) for boy in range(len(grid))}


        for boy in range(len(grid)):
            if boy not in matched_boy:
                self.match(boy, adj_lists, matched_boy, matched_girl, set())

        return len(matched_girl)
