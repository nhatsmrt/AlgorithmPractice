class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        self.reflection = {"8": "8", "6": "9", "9": "6", "1": "1", "0": "0"}
        self.same = set(["0", "1", "8"])

        ret = []
        cur_num = []
        self.complete_number(cur_num, n, ret)
        return ret

    def complete_number(self, cur_num: List[str], n, ret: List[str]):
        if len(cur_num) == n:
            # done
            ret.append(''.join(cur_num))
        elif len(cur_num) == n // 2 and n % 2 == 1:
            for dig in self.same:
                cur_num.append(dig)
                self.complete_number(cur_num, n, ret)
                cur_num.pop()
        elif len(cur_num) >= n // 2:
            cur_num.append(self.reflection[cur_num[n - 1 - len(cur_num)]])
            self.complete_number(cur_num, n, ret)
            cur_num.pop()
        else:
            # first digit:
            for dig in self.reflection:
                if dig != "0" or len(cur_num) > 0:
                    cur_num.append(dig)
                    self.complete_number(cur_num, n, ret)
                    cur_num.pop()
        
