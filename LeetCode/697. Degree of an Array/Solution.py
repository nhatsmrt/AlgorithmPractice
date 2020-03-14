class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(n)
        index = {}
        # keep track of the start indices, lengths of subarray
        # containing all occurences, and frequency of values

        max_freq = 0
        ret = 100000

        for i in range(len(nums)):
            num = nums[i]
            if num not in index:
                index[num] = [i, 1, 1]
            else:
                index[num][1] = i - index[num][0] + 1
                index[num][2] += 1

            if index[num][2] > max_freq or index[num][2] == max_freq and index[num][1] < ret:
                max_freq = index[num][2]
                ret = index[num][1]

        return ret
        
