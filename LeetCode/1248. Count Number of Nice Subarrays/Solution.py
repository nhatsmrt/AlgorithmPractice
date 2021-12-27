class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Time and Space Complexity: O(N)
        prefix_odd = list(accumulate(map(lambda x: x % 2, nums)))

        cnter = Counter()
        cnter[0] = 1
        ret = 0

        for prefix_cnt in prefix_odd:
            ret += cnter[prefix_cnt - k]
            cnter[prefix_cnt] += 1

        return ret
