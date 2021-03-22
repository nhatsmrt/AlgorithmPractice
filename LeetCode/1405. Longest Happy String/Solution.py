class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Time Complexity: O((a + b + c) log(a + b + c))
        # Space Complexity: O(1)

        # Greedy: select the character with highest count remaining available

        prev, prev_cnt = "", 0
        remaining = [(-a, "a"), (-b, "b"), (-c, "c")]
        remaining = list(filter(lambda pair: pair[0] != 0, remaining))
        heapq.heapify(remaining)

        ret = []
        while remaining:
            remain, char = heapq.heappop(remaining)

            if char == prev and prev_cnt == 2:
                if not remaining:
                    return "".join(ret)
                else:
                    next_remain, next_char = heapq.heappop(remaining)
                    ret.append(next_char)

                    heapq.heappush(remaining, (remain, char))
                    prev, prev_cnt = next_char, 1
                    if next_remain < -1:
                        heapq.heappush(remaining, (next_remain + 1, next_char))

            else:
                if prev == char:
                    prev_cnt += 1
                else:
                    prev_cnt = 1

                prev = char
                ret.append(char)

                if remain < -1:
                    heapq.heappush(remaining, (remain + 1, char))


        return "".join(ret)
