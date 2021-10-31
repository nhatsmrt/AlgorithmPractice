class Solution:
    def reorganizeString(self, S: str) -> str:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        freq_dict = {}
        for char in S:
            freq_dict[char] = freq_dict.get(char, 0) + 1

        priority = [(-freq_dict[char], char) for char in freq_dict]
        heapq.heapify(priority)
        ret = []

        while len(priority) > 0:
            freq, char = heapq.heappop(priority)

            if len(ret) > 0 and ret[-1] == char:
                if len(priority) > 0:
                    other_freq, other_char = heapq.heappop(priority)
                    heapq.heappush(priority, (freq, char))

                    freq, char = other_freq, other_char
                else:
                    return ""

            ret.append(char)

            if freq < -1:
                heapq.heappush(priority, (freq + 1, char))

        return ''.join(ret)
