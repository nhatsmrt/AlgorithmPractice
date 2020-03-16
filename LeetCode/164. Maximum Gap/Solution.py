class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Time and Space Complexity: O(N)
        if len(nums) < 2:
            return 0

        buckets = [[] for i in range(len(nums) + 1)]
        minrange = 1000000000
        maxrange = -1000000000


        for num in nums:
            minrange = min(minrange, num)
            maxrange = max(maxrange, num)

        if minrange == maxrange:
            return 0

        buckets[0].append(minrange)
        buckets[-1].append(maxrange)
        bucket_width = (maxrange - minrange) / (len(buckets) - 1)

        for num in nums:
            if num > minrange and num < maxrange:
                bucket_ind = int((num - minrange) / bucket_width)
                buckets[bucket_ind].append(num)

        extreme_dict = {}
        for i in range(len(buckets)):
            if len(buckets[i]) > 0:
                minrange = 1000000000
                maxrange = -1000000000
                for num in buckets[i]:
                    minrange = min(minrange, num)
                    maxrange = max(maxrange, num)
                extreme_dict[i] = (minrange, maxrange)

        start = 0
        ret = 0

        while start < len(buckets):
            if len(buckets[start]) != 0:
                start += 1
            else:
                end = start
                while end + 1 < len(buckets) and len(buckets[end + 1]) == 0:
                    end += 1

                candidate = extreme_dict[end + 1][0] - extreme_dict[start - 1][1]
                ret = max(candidate, ret)

                start = end + 1

        return ret



                
