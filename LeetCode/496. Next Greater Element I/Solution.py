class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time and Space Complexity: O(M + N)

        index = {}
        for i, num in enumerate(nums2):
            index[num] = i

        next_greater_element = []
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                next_greater_element.append(stack[-1])
            else:
                next_greater_element.append(-1)

            stack.append(num)

        next_greater_element = next_greater_element[::-1]
        ret = []

        for num in nums1:
            ret.append(next_greater_element[index[num]])

        return ret
