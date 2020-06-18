class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations)

        while low < high:
            h = high - (high - low) // 2

            ind = len(citations) - h

            if citations[ind] >= h:
                low = h
            else:
                high = h - 1

        return low

        
