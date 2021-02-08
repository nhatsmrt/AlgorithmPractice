class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        def get_index(lst):
            ret = {}

            for i, res in enumerate(lst):
                ret[res] = i

            return ret

        index1 = get_index(list1)
        index2 = get_index(list2)

        ret = []
        ret_sum = 10000000

        for res in index1:
            if res in index2:
                if index1[res] + index2[res] == ret_sum:
                    ret.append(res)
                elif index1[res] + index2[res] < ret_sum:
                    ret_sum = index1[res] + index2[res]
                    ret = [res]

        return ret
