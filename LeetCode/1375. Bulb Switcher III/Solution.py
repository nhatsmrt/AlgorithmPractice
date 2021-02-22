class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)

        cur_max_light_on = 0
        ret = 0

        for mom, light_ind in enumerate(light):
            cur_max_light_on = max(cur_max_light_on, light_ind)
            if cur_max_light_on == mom + 1:
                ret += 1


        return ret
