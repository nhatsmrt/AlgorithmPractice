class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # Greedy: among remaining labels, select one with highest values
        # Proof: trivial cut-and-paste

        index = {}

        for val, label in zip(values, labels):
            if label not in index:
                index[label] = []

            index[label].append(val)

        remaining = []
        for label in index:
            num_selected = min(len(index[label]), use_limit)
            selected = sorted(index[label])[-num_selected:]
            remaining.append((-selected[-1], label, selected[:-1]))

        heapq.heapify(remaining)
        ret = 0
        for _ in range(num_wanted):
            if not remaining:
                return ret

            value, label, selected = heapq.heappop(remaining)

            ret += -value

            if selected:
                new_value = -selected.pop()
                heapq.heappush(remaining, (new_value, label, selected))

        return ret
