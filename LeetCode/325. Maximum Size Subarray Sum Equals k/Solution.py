class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Time and Space Complexity: O(n)

        prefixes = [0]
        for num in nums:
            prefixes.append(num + prefixes[-1])

        inverted_index = {}
        length = 0
        for i in range(len(prefixes)):
            if prefixes[i] - k in inverted_index:
                length = max(length, i - inverted_index[prefixes[i] - k])

            if prefixes[i] not in inverted_index:
                inverted_index[prefixes[i]] = i

        return length
        
