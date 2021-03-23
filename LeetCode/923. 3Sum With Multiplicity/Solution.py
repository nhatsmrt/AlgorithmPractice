class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(N)

        MOD = 1000000007
        counter = Counter(arr)
        arr = sorted([(val, counter[val]) for val in counter])


        ret = 0
        for i, (first, first_cnt) in enumerate(arr):
            if first * 3 == target:
                ret += first_cnt * (first_cnt - 1) * (first_cnt - 2) // 6
                ret %= MOD

            sub_cnter = {val: cnt for val, cnt in arr[i + 1:]}
            if target - first * 2 in sub_cnter:
                second_cnt = sub_cnter[target - first * 2]
                ret += second_cnt * (first_cnt - 1) * first_cnt // 2
                ret %= MOD

            for second in sub_cnter:
                second_cnt = sub_cnter[second]
                third = target - first - second

                if second == third:
                    ret += first_cnt * (second_cnt - 1) * second_cnt // 2
                    ret %= MOD
                elif second < third and third in sub_cnter:
                    third_cnt = sub_cnter[third]
                    ret += first_cnt * second_cnt * third_cnt
                    ret %= MOD

        return ret
