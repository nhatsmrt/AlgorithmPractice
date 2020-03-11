class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # If we map 0 to -1, then the problem become finding longest contiguous array
        # with sum 0

        # Making the prefix sum array of transformed array, the problem becomes
        # finding the furthest pair of points i j such that prefix[i] = prefix[j]

        # This can be solved using a index (map from value to (first) location)

        # Time and Space Complexity: O(n)

        if len(nums) == 0:
            return 0

        sign = lambda x: -1 if x == 0 else 1
        prefixes = [0]
        for num in nums:
            prefixes.append(sign(num) + prefixes[-1])

        index = {}

        ret = 0
        for i in range(len(prefixes)):
            if prefixes[i] in index:
                ret = max(ret, i - index[prefixes[i]])
            else:
                index[prefixes[i]] = i

        return ret
