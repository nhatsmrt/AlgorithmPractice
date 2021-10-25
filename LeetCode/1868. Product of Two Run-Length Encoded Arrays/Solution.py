class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(|encoded1| + |encoded2|)
        # Space Complexity: O(1) extra space,  O(|encoded1| + |encoded2|) for result

        ret = []

        i = 0
        rem_1 = encoded1[i][1]

        j = 0
        rem_2 = encoded2[j][1]

        ret = []
        while i < len(encoded1) and j < len(encoded2):
            cnt = min(rem_1, rem_2)
            prod = encoded1[i][0] * encoded2[j][0]

            if not ret or ret[-1][0] != prod:
                ret.append([prod, cnt])
            else:
                ret[-1][1] += cnt

            rem_1 -= cnt
            rem_2 -= cnt

            if not rem_1:
                i += 1

                if i < len(encoded1):
                    rem_1 = encoded1[i][1]

            if not rem_2:
                j += 1

                if j < len(encoded2):
                    rem_2 = encoded2[j][1]

        return ret
