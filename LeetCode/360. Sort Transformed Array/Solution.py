class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # Time and Space Complexity: O(N)
        def f(x): return a * x ** 2 + b * x + c
        ret = []
        start, end = 0, len(nums) - 1

        while start <= end:
            start_val, end_val = f(nums[start]), f(nums[end])

            if a > 0:
                if start_val > end_val:
                    ret.append(start_val)
                    start += 1
                else:
                    ret.append(end_val)
                    end -= 1
            else:
                if start_val < end_val:
                    ret.append(start_val)
                    start += 1
                else:
                    ret.append(end_val)
                    end -= 1

        for i in range(len(nums) - 1):
            if ret[i] > ret[i + 1]:
                return ret[::-1]

        return ret
