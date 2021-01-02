class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # Time Complexity: O(|arr| + |pieces|)
        # Space Complexity: O(|pieces|)

        initial = {piece[0]: piece for piece in pieces}

        i = 0
        while i < len(arr):
            if arr[i] not in initial:
                return False

            piece = initial[arr[i]]

            if len(arr) - i < len(piece):
                return False

            for j in range(len(piece)):
                if piece[j] != arr[i + j]:
                    return False

            i += len(piece)

        return True
