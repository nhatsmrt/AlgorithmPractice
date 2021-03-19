class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Time and Space Complexity: O(|s| + k)

        # Greedy: Select character with largest remaining count not in cooldown
        # This can be proved with cut-and-paste argument
        # Consider the 1st error: suppose instead of c1, we should have selected c2
        # if # of remaining c1s == # of remaining c2s, we can swap all c2 with c1 in the feasible solution
        # Otherwise, #c1 > #c2, so there exists a c1 in the optimal solution such that
        # #c1 (before and including it) == #c2 (before it) + 1
        # swap all the c1 and c2 before it one by one.

        counts = Counter(iter(s))
        remaining = [[-counts[key], key] for key in counts]
        heapq.heapify(remaining)

        cooldown = collections.deque()
        ret = []

        while remaining:
            neg_cnt, char = heapq.heappop(remaining)
            ret.append(char)
            neg_cnt += 1

            if k > 1:
                if len(cooldown) == k - 1:
                    ready_cnt, ready_char = cooldown.popleft()

                    if ready_cnt < 0:
                        heapq.heappush(remaining, [ready_cnt, ready_char])


                cooldown.append((neg_cnt, char))
            elif neg_cnt < 0:
                heapq.heappush(remaining, [neg_cnt, char])


        for (cnt, char) in cooldown:
            if cnt:
                return ""

        return "".join(ret)
