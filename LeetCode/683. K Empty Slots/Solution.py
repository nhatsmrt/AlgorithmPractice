INF = 1000000


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        # Time and Space Complexity: O(N)

        light_time = [None] * len(bulbs)

        for day, bulb in enumerate(bulbs):
            light_time[bulb - 1] = day + 1

        first_smaller_left = []
        first_smaller_right = []
        stack = []

        for i, value in enumerate(light_time):
            while stack and stack[-1][0] >= value:
                stack.pop()

            if stack:
                first_smaller_left.append(stack[-1][1])
            else:
                first_smaller_left.append(-1)

            stack.append((value, i))

        stack = []
        for i in range(len(bulbs) - 1, - 1, -1):
            value = light_time[i]

            while stack and stack[-1][0] >= value:
                stack.pop()

            if stack:
                first_smaller_right.append(stack[-1][1])
            else:
                first_smaller_right.append(len(bulbs))

            stack.append((value, i))

        first_smaller_right = list(reversed(first_smaller_right))

        ret = INF
        for start in range(len(bulbs) - k - 1):
            end = start + k + 1

            if first_smaller_right[start] >= end and first_smaller_left[end] <= start:
                ret = min(ret, max(light_time[start], light_time[end]))


        if ret == INF:
            return -1

        return ret
