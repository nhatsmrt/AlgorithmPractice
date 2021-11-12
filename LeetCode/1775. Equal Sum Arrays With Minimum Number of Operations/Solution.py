class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # Time and Space Complexity: O(N)

        diff = sum(nums2) - sum(nums1)
        cnter1 = Counter(nums1)
        cnter2 = Counter(nums2)

        i = 1
        ret = 0

        while diff and i < 6:
            if diff > 0: # increase nums1, decrease nums2
                changable = cnter1[i] + cnter2[7 - i]
                changed = min(changable * (6 - i), diff)
            else:
                changable = cnter1[7 - i] + cnter2[i]
                changed = max(-changable * (6 - i), diff)

            diff -= changed
            ret += math.ceil(abs(changed) / (6 - i))
            i += 1

        if diff:
            return -1

        return ret
