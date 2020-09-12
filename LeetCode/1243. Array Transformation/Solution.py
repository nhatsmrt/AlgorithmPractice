class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True

        while changed:
            arr, changed = self.transform(arr)

        return arr


    def transform(self, arr: List[int]):
        new_arr = []
        changed = False

        for i in range(len(arr)):
            val = arr[i]

            if i > 0 and i < len(arr) - 1:
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    val -= 1
                    changed = True
                elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    val += 1
                    changed = True

            new_arr.append(val)

        return new_arr, changed
