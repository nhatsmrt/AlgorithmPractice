class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # Time Complexity: O(B log B + W)
        # Space Complexity: O(1)

        # Greedy: push the boxes in the order of height, as far as possible into the warehouse
        # Correctness: cut-and-paste/certifier proof.

        boxes.sort()

        # find tallest height that can fit in ith slot of warehouse
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i - 1])

        end = len(warehouse) - 1
        ret = 0

        for box in boxes:
            while end >= 0 and warehouse[end] < box:
                end -= 1

            if end >= 0:
                ret += 1
                end -= 1

        return ret
