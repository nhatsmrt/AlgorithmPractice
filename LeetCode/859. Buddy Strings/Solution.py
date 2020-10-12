class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # Time and Space Complexity: O(N)

        if len(A) != len(B):
            return False

        diff_inds = []

        for i, (char1, char2) in enumerate(zip(A, B)):
            if char1 != char2:
                diff_inds.append(i)

        return (not diff_inds and len(set(iter(A))) < len(A)) or (len(diff_inds) == 2 and A[diff_inds[0]] == B[diff_inds[1]] and A[diff_inds[1]] == B[diff_inds[0]])
