class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reflection = {"8": "8", "6": "9", "9": "6", "1": "1", "0": "0"}

        for i in range(len(num)):
            if num[i] not in reflection:
                return False

            if reflection[num[i]] != num[len(num) - 1 - i]:
                return False

        return True
