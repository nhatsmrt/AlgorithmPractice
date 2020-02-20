class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_elements = 0
        i = 0
        last_ind = -1

        while num_elements < len(arr):
            if arr[i] != 0:
                num_elements += 1
            else:
                num_elements += 2
            i += 1

        i -= 1
        copy_ind = len(arr) - 1
        if num_elements == len(arr) + 1:
            arr[copy_ind] = 0
            i -= 1
            num_elements -= 2
            copy_ind -= 1

        while i >= 0:
            if arr[i] != 0:
                arr[copy_ind] = arr[i]
                i -= 1
                copy_ind -= 1
            else:
                arr[copy_ind] = arr[copy_ind - 1] = 0
                i -= 1
                copy_ind -= 2
