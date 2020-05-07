class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # diff[i] = arr[i] - arr[i - 1]
        # (arr[-1] = 0)
        # increment a[i:j + 1] by increasing diff[i] and decreasing diff[j + 1]

        # Time and space complexity: O(N)

        diff = [0] * length
        for update in updates:
            diff[update[0]] += update[2]

            if update[1] + 1 < length:
                diff[update[1] + 1] -= update[2]

        ret = []
        cumsum = 0

        for i in range(length):
            cumsum += diff[i]
            ret.append(cumsum)

        return ret
