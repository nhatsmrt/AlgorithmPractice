class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # Greedy: consider each element in sorted order of B
        # assign the smallest available number in A that is greater than it
        # Proof: cut-and-paste (trivial)

        A_sorted = sorted(enumerate(A), key=lambda pair: pair[1])
        B_sorted = sorted(enumerate(B), key=lambda pair: pair[1])

        assignment = []
        aind = 0
        bind = 0

        while aind < len(A) and bind < len(B):
            if A_sorted[aind][1] > B_sorted[bind][1]:
                assignment.append((B_sorted[bind][0], A_sorted[aind][0]))
                aind += 1
                bind += 1
            else:
                aind += 1

        ret = [None] * len(A)
        unassigned_new = set(range(len(A)))
        unassigned_original = set(range(len(A)))
        for new_ind, original_ind in assignment:
            ret[new_ind] = A[original_ind]
            unassigned_original.remove(original_ind)
            unassigned_new.remove(new_ind)

        for new_ind, original_ind in zip(unassigned_new, unassigned_original):
            ret[new_ind] = A[original_ind]

        return ret
