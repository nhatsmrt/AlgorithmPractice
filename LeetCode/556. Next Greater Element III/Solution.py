class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Time and Space Complexity: O(|digit|) = O(1)

        digits = self.to_digits(n)
        limit = 2 ** 31 - 1

        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                self.reverse(digits, i + 1)
                self.swap(digits, i, self.find(digits, i + 1, digits[i]))

                ret = self.to_num(digits)

                if ret <= limit:
                    return ret
                else:
                    return -1

        else:
            return -1


    def find(self, nums, start, target):
        low = start
        high = len(nums) - 1


        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return low


    def reverse(self, nums: List[int], start: int):
        for i in range(start, (start + len(nums)) // 2):
            self.swap(nums, i, len(nums) - i + start - 1)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


    def to_digits(self, n: int) -> List[int]:
        ret = []

        while n > 0:
            ret.append(n % 10)
            n //= 10

        return ret[::-1]

    def to_num(self, digits: List[int]) -> int:
        ret = 0

        for dig in digits:
            ret = ret * 10 + dig


        return ret
