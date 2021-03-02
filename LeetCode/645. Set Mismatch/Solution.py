class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        n = len(nums)
        xor = 0

        for i in range(1, n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        rightmost = xor & ~(xor - 1)

        # Divide range(1, n + 1) into 2 sets:
        # one set containing numbers with 1 at rightmost
        # and the other containing numbers with 0 at rightmost
        # x and y will belong to two different sets

        # we will find xor of (set1 intersect nums, set1) and (set2 intersect nums, set2)
        # one of these will contain the duplicate

        xor1 = 0
        xor2 = 0

        for i in range(1, n + 1):
            if (rightmost & i) > 0:
                xor1 ^= i
            else:
                xor2 ^= i


        for num in nums:
            if (rightmost & num) > 0:
                xor1 ^= num
            else:
                xor2 ^= num

        for num in nums:
            if xor1 == num:
                # xor1/num is the repeated value
                return [xor1, xor ^ xor1]

        return [xor2, xor ^ xor2]
