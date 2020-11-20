class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Time complexity: O(N)
        # Space complexity: O(1)

        if not nums:
            return False

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] == target or nums[low] == target:
                return True

            if nums[mid] == nums[low]:
                # cannot binary search, because unclear if mid is in first or second part
                # but we do know that either way, we can eliminate low
                # since nums[low] = nums[mid] != target
                low += 1
            elif nums[mid] > nums[low]:
                # mid and start belong to the same part
                if target < nums[low]:
                    # mid and low are in different part from target
                    low = mid + 1
                else:
                    # mid, low, target are in the same part
                    if nums[mid] < target:
                        low = mid + 1
                    else:
                        high = mid
            else:
                # low and mid are in different parts
                if target > nums[low]:
                    # low and target in the different part from mid
                    high = mid - 1
                else:
                    if nums[mid] < target:
                        low = mid + 1
                    else:
                        high = mid

        return nums[low] == target
