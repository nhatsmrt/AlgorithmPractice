class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Time and Space Complexity: O(N)

        ret = [""] * len(s)

        for char, new_ind in zip(s, indices):
            ret[new_ind] = char

        return "".join(ret)
