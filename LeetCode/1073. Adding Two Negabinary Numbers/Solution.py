class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Time and Space Complexity: O(M + N)

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        ret = []
        carry = 0
        i = 0

        while i < len(arr1) or i < len(arr2):
            total = carry

            if i < len(arr1):
                total += arr1[i]

            if i < len(arr2):
                total += arr2[i]

            if total == -1:
                # (-1) * (-2)^x = (-2)^(x + 1) + (-2)^x
                ret.append(1)
                carry = 1
            elif total == 0:
                ret.append(0)
                carry = 0
            elif total == 1:
                ret.append(1)
                carry = 0
            elif total == 2:
                ret.append(0)
                carry = -1
            else: # total == 3
                ret.append(1)
                carry = -1

            i += 1


        if carry == -1:
            ret.extend([1, 1])
        elif carry == 1:
            ret.append(1)
        elif carry == 2:
            # 2 * (-2)^x = (-2)^(x + 2) + (-2)^(x + 1)
            ret.extend([0, 1, 1])

        while len(ret) > 1 and not ret[-1]:
            ret.pop()

        return ret[::-1]
