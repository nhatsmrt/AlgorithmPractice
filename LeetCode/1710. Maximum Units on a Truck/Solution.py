class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(1)

        # Greedy: load the boxes in decreasing order of units
        # Proof: cut-and-paste

        boxTypes.sort(key=lambda pair: -pair[-1])
        ret = 0
        remaining = truckSize
        box_ind = 0

        while box_ind < len(boxTypes) and remaining > 0:
            ret += boxTypes[box_ind][1] * min(remaining, boxTypes[box_ind][0])
            remaining -= min(remaining, boxTypes[box_ind][0])
            box_ind += 1

        return ret
