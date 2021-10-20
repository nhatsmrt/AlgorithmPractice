class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        ret = []

        i = 0
        j = 0
        k = 0

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                ret.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                min_val = min(arr1[i], arr2[j], arr3[k])

                if arr1[i] == min_val:
                    i += 1

                if arr2[j] == min_val:
                    j += 1

                if arr3[k] == min_val:
                    k += 1

        return ret
