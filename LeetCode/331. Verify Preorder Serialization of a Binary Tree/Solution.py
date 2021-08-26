class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Time and Space Complexity: O(N)
        values = preorder.split(",")
        return self.validate(values, 0) == len(values)

    def validate(self, values: List[str], i: int):
        if values[i] == "#":
            return i + 1 # null node, no children

        if i + 1 == len(values):
            return None

        right_start = self.validate(values, i + 1)
        if right_start is None or right_start == len(values):
            return None

        return self.validate(values, right_start)
