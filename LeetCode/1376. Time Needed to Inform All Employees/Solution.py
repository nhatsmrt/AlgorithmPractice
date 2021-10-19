class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Time and Space Complexity: O(N)
        subords = {}

        for subord, manager in enumerate(manager):
            if manager != -1:
                if manager not in subords:
                    subords[manager] = []

                subords[manager].append(subord)

        return self.transmit(headID, subords, informTime)

    def transmit(self, id, subords, informTime):
        if not subords.get(id, []):
            return 0

        return informTime[id] + max(self.transmit(subord, subords, informTime) for subord in subords[id])
