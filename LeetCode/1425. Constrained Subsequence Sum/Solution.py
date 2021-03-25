class IndexedPQ:
    def __init__(self):
        self.key_to_ind = {}
        self.ind_to_key = {}
        self.priorities = []

    def insert(self, key: int, priority: int):
        self.key_to_ind[key] = len(self.priorities)
        self.ind_to_key[len(self.priorities)] = key
        self.priorities.append(priority)
        self.sift_up(len(self.priorities) - 1)

    def get_max(self):
        return self.priorities[0]

    def sift_up(self, ind: int):
        if ind == 0:
            return

        par_ind = (ind - 1) // 2
        par_priority, priority = self.priorities[par_ind], self.priorities[ind]

        if par_priority < priority:
            # swap ind and par_ind
            self.swap(par_ind, ind)
            self.sift_up(par_ind)

    def swap(self, ind1, ind2):
        key1, key2 = self.ind_to_key[ind1], self.ind_to_key[ind2]
        priority1, priority2 = self.priorities[ind1], self.priorities[ind2]

        self.priorities[ind1] = priority2
        self.priorities[ind2] = priority1

        self.key_to_ind[key1] = ind2
        self.key_to_ind[key2] = ind1

        self.ind_to_key[ind1] = key2
        self.ind_to_key[ind2] = key1


    def remove_key(self, key: int):
        ind = self.key_to_ind[key]

        self.swap(ind, len(self.priorities) - 1)
        self.key_to_ind.pop(key)
        self.ind_to_key.pop(len(self.priorities) - 1)
        self.priorities.pop()

        self.sift_down(ind)


    def sift_down(self, ind: int):
        if ind * 2 + 1 >= len(self.priorities):
            return
        elif ind * 2 + 2 >= len(self.priorities):
            child_ind = ind * 2 + 1
        else:
            left_ind = ind * 2 + 1
            right_ind = ind * 2 + 2

            child_ind = left_ind if self.priorities[left_ind] >= self.priorities[right_ind] else right_ind

        if self.priorities[ind] < self.priorities[child_ind]:
            self.swap(ind, child_ind)
            self.sift_down(child_ind)

    def __len__(self):
        return len(self.priorities)


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # Let dp[i] be the max constrained subseq sum starting from nums[i]
        # dp[i] = nums[i] + max(0, dp[i + 1], ..., dp[i + k - 1])
        # answer = max_i dp[i]

        pq = IndexedPQ()
        ret = -100000000000

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]

            if len(pq) == 0:  # base case
                solution = num
            else:
                solution = num + max(0, pq.get_max())

            if len(pq) == k:
                pq.remove_key(i + k)

            ret = max(ret, solution)
            pq.insert(i, solution)

        return ret
