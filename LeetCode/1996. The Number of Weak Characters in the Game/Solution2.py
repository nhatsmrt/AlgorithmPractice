class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        properties.sort(key=lambda prop: (prop[0], -prop[1]))
        frontier = []
        ret = 0

        for att, defend in properties:
            # Add point to frontier:
            if frontier and frontier[-1][0] == att:
                cnt = 1
                stack = frontier[-1][1]

                while stack and stack[-1][0] <= defend:
                    cnt += stack.pop()[1]

                stack.append((defend, cnt))
            else:
                frontier.append((att, [(defend, 1)]))

            top_stack = frontier.pop()

            while frontier:
                cand_stack = frontier[-1][1]

                if not cand_stack:
                    frontier.pop()
                elif cand_stack[-1][0] >= defend:
                    break
                else:
                    ret += cand_stack.pop()[1]

            # re-add top-of-frontier
            frontier.append(top_stack)

        return ret
